# google-protorpc
--------------

mirror of http://code.google.com/p/google-protorpc/ without Google App Engine dependencies.


### Install with pip

    pip install https://github.com/gregorynicholas/google-protorpc/tarball/master


### Try the HelloService 

A simple service called HelloService is defined in demos/hello_service.py.
Simply start the server on port 8000 by running:

    python demo/server.py

In another terminal you can run the client with:

    python demo/client.py

The API is also accessible via JSON POST:

    curl -H 'content-type:application/json' \
      -d '{"my_name": "Matt"}' \
      http://localhost:8000/HelloService.Hello
