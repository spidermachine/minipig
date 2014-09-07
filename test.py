# !/usr/bin/python
# vim: set fileencoding=utf8 :
#
__author__ = 'keping'

import threading

from minipig.processor import AbsractProcessor
from minipig.executor import Executor
from minipig.request import Request


class DefaultProcessor(AbsractProcessor):

    def process(self, request):
        print threading.current_thread
        print request.result

    def accepted(self, request):

        return True


class DefaultRequest(Request):

    def __init__(self, index):

        self.result = index

if __name__ == "__main__":

    Executor.get_executor().register_processor(DefaultProcessor())
    #sync between threads
    for i in xrange(1000):
        request = DefaultRequest(index=i)
        Executor.get_executor().execute(request)
        request.get_result()

    #async
    for i in xrange(1000):
        request = DefaultRequest(index=i)
        Executor.get_executor().execute(request)


    #run in same thread
    for i in xrange(1000):
        request = DefaultRequest(index=i)
        request.async = False
        Executor.get_executor().execute(request)

    print threading.currentThread()

    while 1:
        pass