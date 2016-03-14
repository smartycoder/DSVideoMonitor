
from subprocess import call
from watchdog.events import PatternMatchingEventHandler, os
from babelfish import Language
from subliminal import download_best_subtitles, save_subtitles, scan_video


class VideoFileHandler(PatternMatchingEventHandler):

    def __init__(self, patterns=None, ignore_patterns=None,
                 ignore_directories=False, case_sensitive=False):
        super(PatternMatchingEventHandler, self).__init__()

        self._patterns = patterns
        self._ignore_patterns = ignore_patterns
        self._ignore_directories = ignore_directories
        self._case_sensitive = case_sensitive
        self._logger = None
        self._languages = ["eng"]
        self._modified_files = []

        self.run_indexer = False


        # events
        self.on_file_processed = Event()
        self.on_error = Event()

    def set_logger(self, logger):
        self._logger = logger

    def set_languages(self, languages):
        self._languages = languages

    def do_index(self, event, args):

        subtitles_found = None

        try:
            self._logger.info("Event: " + event.event_type)
            self._logger.info("Indexing file: " + event.src_path)

            if self.run_indexer:
                call(["synoindex", args, event.src_path])

            filename, file_extension = os.path.splitext(event.src_path)
            if os.path.isfile(filename + ".srt"):
                subtitles_found = "Existing"
                self._logger.info("Subtitles already exists.")

            if not subtitles_found:
                self._logger.info("Downloading subtitles ...")
                videos = [scan_video(event.src_path)]

                for lng in self._languages:
                    if subtitles_found:
                        break

                    self._logger.info("Downloading best subtitles for language code: " + lng)
                    subtitles = download_best_subtitles(videos, {Language(lng)}, min_score=0, hearing_impaired=False, only_one=True)

                    for v in videos:
                        self._logger.info(subtitles[v])
                        downloaded = save_subtitles(v, subtitles[v], True)

                        if len(downloaded) > 0:
                            subtitles_found = lng
                            for sub in downloaded:
                                self._logger.info("Subtitles found using provider: " + sub.provider_name)
                                # self.subtitles_downloaded.fire(v, sub)
                        else:
                            self._logger.warning("Subtitles not found for language code " + lng)
                            # self.subtitles_missing.fire(v)

            self.on_file_processed.fire(event.src_path, self.run_indexer, subtitles_found)

        except Exception as e:
            self._logger.error(str(e))
            self.on_error(event.src_path, str(e))

    def on_created(self, event):
        self.do_index(event, "-a")

    def on_deleted(self, event):
        self._logger.info("Event: " + event.event_type)
        self._logger.info("Indexing file: " + event.src_path)

        if self.run_indexer:
            try:
                call(["synoindex", "-d", event.src_path])
            except Exception as e:
                self._logger.error(str(e))
                self.on_error(event.src_path, str(e))

    def on_moved(self, event):
        self.do_index(event, "-a")

    def on_modified(self, event):
        if event.src_path not in self._modified_files:
            self._modified_files.append(event.src_path)
            self.do_index(event, "-a")


class Event:
    def __init__(self):
        self.handlers = set()

    def handle(self, handler):
        self.handlers.add(handler)
        return self

    def unhandle(self, handler):
        try:
            self.handlers.remove(handler)
        except:
            raise ValueError("Handler is not handling this event, so cannot unhandle it.")
        return self

    def fire(self, *args, **kargs):
        for handler in self.handlers:
            handler(*args, **kargs)

    def getHandlerCount(self):
        return len(self.handlers)

    __iadd__ = handle
    __isub__ = unhandle
    __call__ = fire
    __len__  = getHandlerCount