import webapp2
from google.cloud import translate
import twilio
from twilio.rest import TwilioRestClient
import twilio.twiml
import os
from config import PHONE_DIC, FROM_PARENTS, MY_PHONE_NUMBER, PARENTS

# Twilio Account Information
TWILIO_ACCOUNT_SID=os.environ.get("TWILIO_ACCOUNT_SID")
TWILIO_AUTH_TOKEN=os.environ.get("TWILIO_AUTH_TOKEN")
TWILIO_NUMBER=os.environ.get("TWILIO_NUMBER")

translate_client = translate.Client()


class Home(webapp2.RequestHandler):
    """A GET Request Handler"""

    def get(self):
        """Receives a GET request"""

        self.response.write('Hello, DevelopHerDevelopHim Viewers!')


class ProcessText(webapp2.RequestHandler):
    """A POST Request Handler"""

    def post(self):
        """Receives a POST request"""

        from_phone_number = self.request.get("From")[1:]
        message = self.request.get("Body").lower()

        to_phone_number, response = process_message(from_phone_number, message)

        send_text_message(to_phone_number, response)


def translates(to_phone_number, message):
    """Makes an API call to translate the message."""

    translation = translate_client.translate(
        message,
        target_language=PHONE_DIC[to_phone_number]['language'])

    return translation[u'translatedText'].encode('utf-8')


def process_message(from_phone_number, message):
    """Processes message, returns from who and translated message"""

    to_phone_number = MY_PHONE_NUMBER

    if from_phone_number == MY_PHONE_NUMBER:
        to_who = message[:3]
        to_phone_number = PARENTS[to_who]
        message = message[3:]

    translated_message = translates(to_phone_number, message)

    # if its from mom or dad, add that its from them in the message
    if from_phone_number != MY_PHONE_NUMBER:
        translated_message = "{}: {}".format(FROM_PARENTS[from_phone_number].upper(), translated_message.encode('utf-8'))

    return (to_phone_number, translated_message)


def send_text_message(phone, message):
    """sends a text message to the phone number"""

    try:
        client = TwilioRestClient(TWILIO_ACCOUNT_SID, TWILIO_AUTH_TOKEN)

        message = client.messages.create(
            body=message,
            to="+"+phone,
            from_=TWILIO_NUMBER
        )
    except twilio.TwilioRestException as e:
        print e

app = webapp2.WSGIApplication([
                        (r'/', Home),
                        (r'/translate', ProcessText)
                        ],
                        debug=True)


def main():
    from paste import httpserver
    httpserver.serve(app, host='127.0.0.1', port='8080')

if __name__ == '__main__':
    main()
