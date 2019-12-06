import os
import psutil
from mitmproxy import ctx, http

class Example:
    def __init__(self):
        self.num = 0
        print(f'init class: {self.__class__.__name__}')
        # formatter = logging.Formatter('%(asctime)s|%(name)s|%(levelname)s: %(message)s')
        # console_handler = logging.StreamHandler()
        # console_handler.setFormatter(formatter)
        # self.log = logging.getLogger()
        # self.log.addHandler(streamHandler)
        
    
    def request(self, flow: http.HTTPFlow) -> None:
        # pretty_url takes the "Host" header of the request into account, which
        # is useful in transparent mode where we usually only have the IP otherwise.
        if "pivotal" in flow.request.pretty_url.lower():
            resp_string = "WHAM! " + flow.request.pretty_url
            flow.response = http.HTTPResponse.make( # Here we respond early and never make the request
                200,  # (optional) status code
                resp_string.encode(),  # (optional) content
                {"Content-Type": "text/html"}  # (optional) headers
            )
        # resp = http.HTTPResponse(
        #     http_version=b"HTTP/2.0",
        #     status_code=200,
        #     reason=b'OK',
        #     headers=flow.request.headers,
        #     content=content I want to send to my device
        # )


    def response(self, flow: http.HTTPFlow) -> None:
        mem_MB = self.get_memory_usage_MB()
        print(f"Memory used: {mem_MB} MB")
        # Remove response headers
        # flow.response.headers.pop('Example Header', None)

        # Modify the response body
        flow.response.content = flow.response.content.replace(
            b'News', 
            b'FAKE News'
        )
    
    def get_memory_usage_MB(self) -> float:
        # return the memory usage in MB
        process = psutil.Process(os.getpid())
        mem = process.memory_info()[0] / float(2 ** 20)
        return mem


addons = [
    Example()
]