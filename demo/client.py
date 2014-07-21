from protorpc import remote
from protorpc import transport

import hello_service


hello_remote = hello_service.HelloService.Stub(
    transport.HttpTransport('http://localhost:8000/HelloService'))
request = hello_service.HelloRequest(my_name='Matt')

print hello_remote.Hello(request).hello
