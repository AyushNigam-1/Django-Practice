from typing import Any


class ExampleMiddleware:
    
    def __init__(self , get_response) -> None:
        self.get_response = get_response
        
    def __call__(self,request, *args: Any, **kwargs):
        response = self.get_response(request)
        # process_exception
        return response