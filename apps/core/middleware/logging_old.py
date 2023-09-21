from django.conf import settings
from django.utils import timezone
from apps.core.logging import Logging
from django.utils.deprecation import MiddlewareMixin




logging = Logging(str(settings.BASE_DIR / "logs" / "req_res_logs.txt"))

def simple_logging_middleware(get_response):
    def middleware(request):
        # TODO: pre-processing
        #print("pre-processing")
        #breakpoint()
        http_method = request.method
        url = request.get_full_path()
        host_port = request.get_host()
        content_type = request.headers['Content_Type']
        user_agent = request.headers['User_Agent']

        msg = f"{http_method}: {host_port}{url} {content_type} {user_agent}"
        logging.info(msg)
        
        response= get_response(request)
        
        # TODO: Post-processing
        
        # TODO: Investigate the response and decide on what to log
        if response.status_code >= 400 and  response.status_code <= 499: # response error
            error_message = f"Response Error: {response.status_code} {response.reason_phrase}"
            logging.error(error_message)
        else:    
        # TODO: Formulate your message
            response_content_type  = response.get('Content-Type', 'N/A')
            response_mesage = f"Response Content Type: {response_content_type}"
        
            # TODO: Log the message using the info level method
            logging.info(response_mesage)
        
        return response
    
    return middleware

# class based middleware
class ViewExecutionTimeMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response
    
    def __call__(self, request):
        
        start_time = timezone.now()
        
        response = self.get_response(request)
        
        total_time = timezone.now() - start_time
        http_method = request.method
        url = request.get_full_path()
        host_port = request.get_host()
        msg = f"EXECUTION TIME {total_time} >> {http_method} | {host_port}{url}"
        
        logging.info(msg)
        
        return response
    
class PrintingNewLineMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response
    
    def __call__(self, request):
        
        response = self.get_response(request)
        
        msg = f"\n"
        
        logging.info(msg)
        
        return response
    
    ''' # Function based middleware
class ViewExecutionTimeMiddleware:
        def process_request(self, request):
            request.start_time = timezone.now()
            
        def process_response(self, request, response):
            total_time = timezone.now() - request.start_time
            http_method = request.method
            url = request.get_full_path()
            host_port = request.get_host()    
            msg = f"EXECUTION TIME {total_time} >> {http_method} | {host_port}{url}"
        
            logging.info(msg)
            
            
        
        def __init__(self, get_response):
            self.get_response = get_response
        
        def __call__(self, request):
            
            start_time = timezone.now()
            
            response = self.get_response(request)
            
            total_time = timezone.now() - start_time
            http_method = request.method
            url = request.get_full_path()
            host_port = request.get_host()
            msg = f"{total_time} >> {http_method} | {host_port}{url}"
            
            logging.info(msg)
            
            return response
            '''
        
        