from abc import ABCMeta, abstractmethod
from logging import Logger

class PushNotificationClient():
    __metaclass__ = ABCMeta

    _api_key = None
    _logger = Logger

    @abstractmethod
    def get_name(self):
        return ""

    @abstractmethod
    def set_api_key(self, api):
        self._api_key = api

    @abstractmethod
    def send_message(self, title, msg):
        pass

    @abstractmethod
    def set_logger(self, logger):
        self._logger = logger
