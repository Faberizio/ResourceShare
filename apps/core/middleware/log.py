import logging

# Get the logging instance
logger = logging.getLogger('logging_mw') # __name__


'''logger.info(msg)
logger.error(msg)
logger.debug(msg)
logger.warning(msg)
logger.critical(msg)
'''

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
        logger.info(msg)
        
        response= get_response(request)
        
        # TODO: Post-processing
        
        # TODO: Investigate the response and decide on what to log
        if response.status_code >= 400 and  response.status_code <= 499: # response error
            error_message = f"Response Error: {response.status_code} {response.reason_phrase}"
            logger.error(error_message)
        else:    
        # TODO: Formulate your message
            response_content_type  = response.get('Content-Type', 'N/A')
            response_mesage = f"Response Content Type: {response_content_type}"
        
            # TODO: Log the message using the info level method
            logger.info(response_mesage)
        
        return response
    
    return middleware
