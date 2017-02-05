import goslate
import twilio
from twilio.rest import TwilioRestClient
import twilio.twiml
import os
from config import PHONE_DIC, PARENTS, FROM_PARENTS, TO_PHONE_NUMBER

# Twilio Account Information
TWILIO_ACCOUNT_SID=os.environ.get("TWILIO_ACCOUNT_SID")
TWILIO_AUTH_TOKEN=os.environ.get("TWILIO_AUTH_TOKEN")
TWILIO_NUMBER=os.environ.get("TWILIO_NUMBER")


def process_message(from_phone_number, message):
    """Returns the translated message"""
    print "in the process message function"

    to_phone_number = TO_PHONE_NUMBER

    if from_phone_number == to_phone_number:
        to_who = message[:3]
        to_phone_number = PARENTS[to_who]
        print "to_who", to_who
        message = message[3:]
        print "message", message

    print "to_phone_number", to_phone_number
    gs = goslate.Goslate()
    print "message:", message
    print "language:", PHONE_DIC[from_phone_number]['language']

    translated_message = gs.translate(message, PHONE_DIC[from_phone_number]['language'])

    if from_phone_number != "+18052525094":
        translated_message = "{}: {}".format(FROM_PARENTS[from_phone_number].upper(), translated_message)

    print "*"*80
    print "done with tranlate function"
    return (to_phone_number, translated_message)


def send_text_message(phone, message):
    """sends a text message to the phone number"""

    print 'sending text message'

    try:
        client = TwilioRestClient(TWILIO_ACCOUNT_SID, TWILIO_AUTH_TOKEN)

        message = client.messages.create(
            body=message,
            to=phone,
            from_=TWILIO_NUMBER
        )
    except twilio.TwilioRestException as e:
        print e


# if my number
        # check if mom or dad
        # translate the rest to korean
        # sends message to if mom or dad
    # if mom or data
        # translate to english
        # send me message with add "from mom or dad"

    # if picture(s)
        # just send it through
