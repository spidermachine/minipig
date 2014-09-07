# !/usr/bin/python
# vim: set fileencoding=utf8 :
#
__author__ = 'keping'

import Queue
import threading


class Executor:

    instance = None

    """
    manage the queue and worker.
    """

    def __new__(cls, *args, **kwargs):

        if not hasattr(cls, "instance"):
            cls.instance = super(Executor, cls).__new__(cls, *args, **kwargs)

        return cls.instance

    def __init__(self, count):
        if not hasattr(self, "queue"):
            self.queue = Queue.LifoQueue()
            self.processors = []
            for i in xrange(count):
                t = threading.Thread(target=self._worker)
                print t
                t.setDaemon(True)
                t.start()

    @staticmethod
    def get_executor():
        if not Executor.instance:
            Executor.instance = Executor(3)
        return Executor.instance

    def _worker(self):
        """
        run in separate thread
        """
        while True:
            request = self.queue.get()
            self.worker(request)

    def worker(self, request):
        """
        handle the request through all processors
        """
        try:
            for processor in self.processors:
                if processor.accepted(request):
                    processor.process(request)
        except Exception as e:
            #TODO print e
            print e
            pass
        finally:
            #waiter be awakened
            request.notify()

    def execute(self, request):
        if request.async:
            self.queue.put(request)
        else:
            self.worker(request)

    def register_processor(self, processor):

        self.processors.append(processor)

