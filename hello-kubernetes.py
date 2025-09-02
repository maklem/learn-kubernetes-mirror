import logging
import os

from flask import Flask

app = Flask(__name__)
COUNTER_FILENAME = "/data/counter"

@app.route("/")
def hello():
    visitor_count = 0
    with open(COUNTER_FILENAME, 'r') as f:
        try: 
            visitor_count = int(f.read())
        except ValueError:
            visitor_count = 0
    visitor_count += 1
    with open(COUNTER_FILENAME, 'w') as f:
        f.write(f"{visitor_count}")

    return f"Hello, Kubernetes on Raspberry Pi 5 from Python!<br /> You are visitor {visitor_count}"

if __name__ == "__main__":
    if not os.path.exists(COUNTER_FILENAME):
        with open(COUNTER_FILENAME, 'w') as f:
            f.write("0")
        logging.warning(f"Creating new counter for {COUNTER_FILENAME=}")


    app.run(host="0.0.0.0", port=5000)
