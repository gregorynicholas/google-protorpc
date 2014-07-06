from protorpc import messages
from protorpc import remote


# Create the request string containing the user's name
class HelloRequest(messages.Message):
    my_name = messages.StringField(1, required=True)


# Create the response string
class HelloResponse(messages.Message):
    hello = messages.StringField(1, required=True)


# Create the RPC service to exchange messages
class HelloService(remote.Service):

    @remote.method(HelloRequest, HelloResponse)
    def Hello(self, request):
        return HelloResponse(
            hello='Hello there, %s!' % request.my_name)
