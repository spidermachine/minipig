minipig
=======
A mini async/sync message process framework with multiple threads.

How to use it
=============
 **process message with synchronous and same thread

    from minipig.request import Request
    from minipig.executor import Executor
    from minipig.processor import AbstractProcessor
    
    # define your request
    class MyRequest(Reqeust):
        ......
    
    # define your processor
    class MyProcessor(AbstractProcessor):
        
        def accepted(self, request):
            return True
        
        def process(self, request):
            ......
            
    # register your processor
    
    Executor.get_instance().register_processor(MyProcessor())
    
    
    # initial your request
    m y_request = MyRequest()
    # handle this request with synchronous and in same thread.
    # hdnel this request with asynchronous and in separate thread when async is True
    my_request.async = False #default is True
    Executor.get_instance().execute(my_request)
    
**process message with asynchronous and separate thread

    message be handle default is asynchronous, within separated thread. when your need to get the result of
    request, just call the method get_result of request. As following code:
    
    my_request = MyRequest()
    # handle this request with asynchronous and in separated thread.
    Executor.get_instance().execute(my_request)
    
    .....
    # need to wait the request through all processors,
    # blocking until the request be completed
    result = my_request.get_result()
    
        
        
