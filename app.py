import os
from flask import Flask
from boarding.views import BordingInstructionsView


app = Flask(__name__)


@app.route("/")
def hello_world():
    return "Hello, World!"


app.add_url_rule(
    "/boardingInstructions",
    view_func=BordingInstructionsView.as_view("boardingInstructions"),
    methods=["POST"],
)


if __name__ == "__main__":
    port = int(os.environ.get("PORT", 8080))
    app.run(host="0.0.0.0", port=port, debug=True)
