# !/usr/bin/python
# vim: set fileencoding=utf8 :
#
__author__ = 'keping'

import abc

class AbsractProcessor:
    """
    handle the request when accepted the request.
    subclass should derive from it, and override all abstract methods
    """
    __metaclass__ = abc.ABCMeta

    @abc.abstractmethod
    def process(self, request):
        pass

    @abc.abstractmethod
    def accepted(self, request):
        pass