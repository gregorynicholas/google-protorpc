from protorpc import remote
from protorpc import transport

import hello_service


hello_remote = transport.HttpTransport('http://localhost:8000/HelloService')
rpc_method_info = remote.get_remote_method_info(hello_service.HelloService.Hello)
request = hello_service.HelloRequest(my_name='Matt')
rpc = hello_remote.send_rpc(rpc_method_info, request)

print rpc.response.hello
