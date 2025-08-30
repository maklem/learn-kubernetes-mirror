from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello, Kubernetes on Raspberry Pi 5 from Python!"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
