#!/usr/bin/env python3


from werkzeug.wrappers import Request, Response

@Request.application
def application(request):
    print(f'This web server is running at {request.remote_addr}')
    return Response('A WSGI generated this response!')

if __name__== '__main__':
    from werkzeug.serving import run_simple
    run_simple(
        hostname= 'localhost',
        port=5555,
        application=application
    )

# The request application is the sole function inside our script.
# You can call it anything other than application
# The @Request.application decorator method tells it to run any code inside of the function in the browser at the location we specify with our development server.

# The run simple() function comes with Werkzeug and runs a server for a one-page app without complications.
# It takes three arguments:
     # - Hostname (defaults to localhost)
     # - Port number (defaults to 8000)  
     # - And application which defined in a function somewhere in the file.
     # - we named our file application