# !/usr/bin/python
# vim: set fileencoding=utf8 :
#
__author__ = 'keping'

import threading


class Request(object):
    """
    request object, subclass should derive from it
    """
    def __new__(cls, *args, **kwargs):
        """
        add default property to the instance of request.
        event for synchronous between threads and result for end the process
        """
        instance = super(Request, cls).__new__(cls, *args, **kwargs)
        #wait for synchronous
        instance.event = threading.Event()
        #asynchronous or synchronous, default is asynchronous
        instance.async = True
        #result when request through all processors
        instance.result = None
        return instance

    def get_result(self):
        """
        blocking when this request in processing,
        return result when end
        """
        self.event.wait()
        return self.result

    def destroy(self):
        del self.event

    def notify(self):
        """
        all threads waiting for it to become true are awakened
        """
        self.event.set()

    def set_result(self, result):
        self.result = result

    def clear(self):
        self.event.clear()