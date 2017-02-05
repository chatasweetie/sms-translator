from flask import Flask, request
from process_translation import process_message, send_text_message

app = Flask(__name__)


@app.route("/", methods=["GET", "POST"])
def communication():
    """Sends text message"""

    from_phone_number = request.values.get('From')
    message = request.values.get("Body").lower()
    print from_phone_number
    print message

    to_phone_number, response = process_message(from_phone_number, message)
    print to_phone_number

    send_text_message(to_phone_number, response)

    return str("resp")


if __name__ == "__main__":

    app.run(debug=True)
