from notification.PushNotificationClient import PushNotificationClient
from pushbullet import PushBullet


class PushbulletClient(PushNotificationClient):

    _client = None

    def set_api_key(self, api):
        self._client = PushBullet(api)

    def send_message(self, title, msg):
        self._client.push_note(title=title, body=msg)


