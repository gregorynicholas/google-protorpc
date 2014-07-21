from protorpc.wsgi import service
from wsgiref.simple_server import make_server

import hello_service


# Map the RPC service and path (/hello)
app = service.service_mappings([
  ('/HelloService', hello_service.HelloService)
])

print "Serving HTTP on port 8000..."
make_server('', 8000, app).serve_forever()
