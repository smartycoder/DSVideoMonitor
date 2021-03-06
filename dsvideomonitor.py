import os
import logging
from time import sleep

import sys
from watchdog.observers import Observer
from DaemonLite import DaemonLite

from notification.PushbulletClient import PushbulletClient
from notification.PushoverClient import PushoverClient
from watchdoghandler import VideoFileHandler

#
# YOU CAN CHANGE SETTINGS
#
video_folder = "/volume1/video/"
patterns = ["*.avi", "*.mkv", "*.mp4"]
languages = ["slv", "eng"]
run_indexer = True  # run synology media indexer

# UNCOMMENT PREFERRED PUSH NOTIFICATION SERVICE
# notifier = None # set not None if disabled
notifier = PushbulletClient()
# notifier = PushoverClient()
notifier.set_api_key("YOUR_KEY")


#
# DON'T CHANGE ANYTHING DOWN HERE
#

# initialize logger
logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)
logger.propagate = False
formatter = logging.Formatter("%(asctime)s - %(levelname)s - %(message)s")

# file handler
fh = logging.FileHandler("/var/log/dsvideomonitor.log", "a")
fh.setLevel(logging.DEBUG)
fh.setFormatter(formatter)
logger.addHandler(fh)
keep_fds = [fh.stream.fileno()]

# console handler
ch = logging.StreamHandler()
ch.setLevel(logging.DEBUG)
ch.setFormatter(formatter)
logger.addHandler(ch)


def file_processed(src_file, indexed, subtitles):
    file_name = os.path.basename(src_file)
    if notifier:
        logger.info("Sending %s notification ..." % notifier.get_name())
        notifier.send_message(file_name, "Indexed: %s\nSubtitles: %s" % (indexed, subtitles))

    logger.info("File %s processed." % file_name)
    logger.info("Done.")
    logger.info("===========================================")


def error_processing(src_file, msg):
    if notifier:
        logger.info("Sending %s notification ..." % notifier.get_name())
        file_name = os.path.basename(src_file)
        notifier.send_message(file_name, "ERROR: " + msg)


class DSVideoMonitor(DaemonLite):

    def run(self):
        logger.info("DSVideoMonitor started.")
        logger.info("Monitoring folder: %s" % video_folder)

        if notifier:
            notifier.set_logger(logger)

        event_handler = VideoFileHandler(patterns=patterns)
        event_handler.set_logger(logger)
        event_handler.set_languages(languages)
        event_handler.run_indexer = run_indexer
        event_handler.set_folder(video_folder)

        # listen to events
        event_handler.on_file_processed += file_processed
        event_handler.on_error += error_processing

        observer = Observer()
        observer.schedule(event_handler, video_folder, recursive=True)
        observer.start()

        while True:
            sleep(1)

#
# create new instance of video monitor and run as daemon
#
video_monitor = DSVideoMonitor("/var/run/dsvideomonitor.pid")

if (len(sys.argv) < 2) or (sys.argv[1] == "start"):
    video_monitor.start()
elif sys.argv[1] == "stop":
    video_monitor.stop()



