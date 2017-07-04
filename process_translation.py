from google.cloud import translate
import twilio
from twilio.rest import TwilioRestClient
import twilio.twiml
import os
from config import PHONE_DIC, PARENTS, FROM_PARENTS, MY_PHONE_NUMBER

# Twilio Account Information
TWILIO_ACCOUNT_SID=os.environ.get("TWILIO_ACCOUNT_SID")
TWILIO_AUTH_TOKEN=os.environ.get("TWILIO_AUTH_TOKEN")
TWILIO_NUMBER=os.environ.get("TWILIO_NUMBER")


def translation(to_phone_number, message):
    """Makes an API call to translate the message.

        >>> translation(18052525094, "banana")
    """
    print "do this one!"
    print to_phone_number
    print message
    print "language:", PHONE_DIC[to_phone_number]['language']

    # Instantiates a client
    translate_client = translate.Client()

    # Translates some text into Russian
    translation = translate_client.translate(
        message,
        target_language=PHONE_DIC[to_phone_number]['language'])

    print "translation:", translation

    return translation[u'translatedText']


def process_message(from_phone_number, message):
    """Returns the translated message

        >>> from_phone_number = u'18052525094'
        >>> message = u'jam banana'
        >>> process_message(from_phone_number, message)
        ('+18052525094', "")
    """

    print "in the process message function"

    from_phone_number = from_phone_number[1:]

    to_phone_number = MY_PHONE_NUMBER
    print "from phone", from_phone_number

    if from_phone_number == MY_PHONE_NUMBER:
        to_who = message[:3]
        print "to who", to_who
        to_phone_number = PARENTS[to_who]
        print "to phone number", to_phone_number
        print "to_who", to_who
        message = message[3:]
        print "message", message

    translated_message = translation(to_phone_number, message)

    # if its from mom or dad, add that its from them in the message
    if from_phone_number != MY_PHONE_NUMBER:
        translated_message = "{}: {}".format(FROM_PARENTS[from_phone_number].upper(), translated_message.encode('utf-8'))

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
            to="+"+phone,
            from_=TWILIO_NUMBER
        )
    except twilio.TwilioRestException as e:
        print e
