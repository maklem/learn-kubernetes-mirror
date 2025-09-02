import logging
import os

from flask import Flask


def create_app(counter_filename: str) -> Flask:
    app = Flask(__name__)

    @app.route("/")
    def hello():
        visitor_count = 0
        with open(counter_filename, 'r') as f:
            try:
                visitor_count = int(f.read())
            except ValueError:
                visitor_count = 0
        visitor_count += 1
        with open(counter_filename, 'w') as f:
            f.write(f"{visitor_count}")

        return f"Hello, Kubernetes on Raspberry Pi 5 from Python!<br /> You are visitor {visitor_count}"

    return app


if __name__ == "__main__":
    COUNTER_FILENAME = "/data/counter"

    app = create_app(counter_filename=COUNTER_FILENAME)

    if not os.path.exists(COUNTER_FILENAME):
        with open(COUNTER_FILENAME, 'w') as f:
            f.write("0")
        logging.warning(f"Creating new counter for {COUNTER_FILENAME=}")

    app.run(host="0.0.0.0", port=5000)
