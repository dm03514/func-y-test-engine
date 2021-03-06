from abc import ABCMeta, abstractmethod


class BaseInitiator(object):
    __metaclass__ = ABCMeta

    @abstractmethod
    def execute(self):
        pass
