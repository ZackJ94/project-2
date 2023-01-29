
"""
Zack's Flask API.
"""

from flask import Flask

import os
import configparser

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

config = parse_config(["credentials.ini", "default.ini"])
message = config["DEFAULT"]["message"]

print(message)

@app.route("/")
def hello():
    return "UOCIS docker demo!\n"

# TODO:
# @app.route("/<string: request>")
# def page(request):
#   if request has illegal chars:
#       send_from_dir(403)
#   if request not found:
#       send_from_dir(404)

# @app.route("/403")
# def error403():
#     pass

# @app.route("/404")
# def error404():
#     pass


if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0') # TODO: port=xxx
