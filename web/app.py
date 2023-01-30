
"""
Zack's Flask API.
"""

import os
import configparser
from flask import Flask, abort, send_from_directory

app = Flask(__name__)

# config parser from project 0
def parse_config(config_paths):
    config_path = None
    for f in config_paths:
        if os.path.isfile(f):
            config_path = f
            break

    if config_path is None:
        raise RuntimeError("Configuration file not found!")

    config = configparser.ConfigParser()
    config.read(config_path)
    return config

# get config from credentials file
config = parse_config(["credentials.ini", "default.ini"])
_port = config["SERVER"]["PORT"]
_debug = config["SERVER"]["DEBUG"]

@app.route("/<string:request>")
def serve(request):

    # check for illegal chars
    if ("~" in request) or (".." in request):
        abort(403)

    elif os.path.isfile(f"./pages/{request}"):
        return send_from_directory("./pages", f"{request}")

    else:
        abort(404)

@app.errorhandler(403)
def illegal(e):
    return send_from_directory("./pages", "403.html"), 403

@app.errorhandler(404)
def notfound(e):
    return send_from_directory("./pages", "404.html"), 404


if __name__ == "__main__":
    app.run(debug=bool(_debug), host='0.0.0.0') # TODO: port=xxxx
