from notification.PushNotificationClient import PushNotificationClient
from pushbullet import PushBullet


class PushbulletClient(PushNotificationClient):

    _client = None

    def set_api_key(self, api):
        try:
            self._client = PushBullet(api)
        except Exception as e:
            self._logger.exception(str(e))

    def send_message(self, title, msg):
        try:
            self._client.push_note(title=title, body=msg)
        except Exception as e:
            self._logger.exception(str(e))


