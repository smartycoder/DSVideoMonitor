from abc import ABCMeta, abstractmethod


class PushNotificationClient():
    __metaclass__ = ABCMeta

    _api_key = None

    @abstractmethod
    def set_api_key(self, api):
        self._api_key = api

    @abstractmethod
    def send_message(self, title, msg):
        pass
