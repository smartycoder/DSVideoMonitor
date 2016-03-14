from pushover import Client
from notification.PushNotificationClient import PushNotificationClient


class PushoverClient(PushNotificationClient):

    _client = None
    _api_token = "aYBH7B28vQCKopoJXGCnwQ5NhPTG9w"

    def set_api_key(self, api):
        try:
            self._client = Client(user_key=api, api_token=self._api_token)
        except Exception as e:
            self._logger.exception(str(e))

    def send_message(self, title, msg):
        try:
            self._client.send_message(title=title, message=msg)
        except Exception as e:
            self._logger.exception(str(e))

    def set_logger(self, logger):
        pass
