from flask import Flask, request
from process_translation import process_message, send_text_message

app = Flask(__name__)


@app.route("/", methods=["GET"])
def homepage():
    """Sends text message"""

    return "hello"


@app.route("/translate", methods=["GET", "POST"])
def communication():
    """Sends text message"""

    from_phone_number = request.values.get('From')[1:]
    message = request.values.get("Body").lower()
    print from_phone_number
    print message

    to_phone_number, response = process_message(from_phone_number, message)
    print "To Phone number", to_phone_number
    print response

    send_text_message(to_phone_number, response)

    return "."


if __name__ == "__main__":

    app.run(debug=True)
