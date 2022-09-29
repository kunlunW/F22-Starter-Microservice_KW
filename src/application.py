from flask import Flask, Response, request
from datetime import datetime
import json
from columbia_student_resource import ColumbiaStudentResource
from flask_cors import CORS

# Create the Flask application object.
app = Flask(__name__,
            static_url_path='/',
            static_folder='static/class-ui/',
            template_folder='web/templates')

CORS(app)

# if a network request comes in and begins with this, then execute the follow def get_health() method
# There's a program that's listening for messages. The @app line is called a route (the route to the function)
# If we execute this python file and it will produce two debugging links, and if we click into one of the links
# it will say "Not Found", this is because we didn't define that route, there's no function there
# But if we add api/health after that, it will work.
# The purpose for this assignment is that we'll take this and upload this to the amazon cloud


@app.get("/api/health")
def get_health():
    t = str(datetime.now())
    msg = {
        "name": "F22-Starter-Microservice",
        "health": "Good",
        "at time": t
    }
    import os
    # print(os.environ)

    # DFF TODO Explain status codes, content type, ... ...
    # I'm returning to some program app that called this function
    # There are three parts to the response object
    # first parameter: data
    # second parameter: status code
    # third parameter: content type, which defines if the data is a string, image, audio file, etc.

    # There are some tools that can be quite useful: postman
    # Browsers send GET request, there are other operations e.g. POST, PUT, DELETE
    result = Response(json.dumps(msg), status=200, content_type="application/json")

    return result

# <uni> is called a path parameter, the function will get student by uni
# This a route that define that network request that comes in the form /api/students/###
# it will execute the following function
# This is also called binding, you have bound a method in python to a specific network point


@app.route("/api/students/<uni>", methods=["GET"])
def get_student_by_uni(uni):

    result = ColumbiaStudentResource.get_by_key(uni)

    if result:
        rsp = Response(json.dumps(result), status=200, content_type="application.json")
    else:
        rsp = Response("NOT FOUND", status=404, content_type="text/plain")

    return rsp

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5011)

