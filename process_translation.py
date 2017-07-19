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


def translates(to_phone_number, message):
    """Makes an API call to translate the message.

        >>> translation(18052525094, "banana")
    """
    print "do this one!"
    print "to_phone_number", to_phone_number
    print message
    print "language:", PHONE_DIC[to_phone_number]['language']

    translation = translate_client.translate(
        message,
        target_language=PHONE_DIC[to_phone_number]['language'])

    print "translation:", translation
    print "translation[u'translatedText']:", translation[u'translatedText']

    return translation[u'translatedText']


def process_message(from_phone_number, message):
    """Processes message, returns from who and translated message

        >>> from_phone_number = u'18052525094'
        >>> message = u'jam banana'
        >>> process_message(from_phone_number, message)
        ('+18052525094', "")
    """
    print "MY_PHONE_NUMBER", MY_PHONE_NUMBER
    to_phone_number = MY_PHONE_NUMBER
    print "to_phone_number", MY_PHONE_NUMBER
    print "from phone", from_phone_number

    if from_phone_number == MY_PHONE_NUMBER[1:]:
        to_who = message[:3]
        print "to who", to_who
        to_phone_number = PARENTS[to_who]
        print "to phone number", to_phone_number
        print "to_who", to_who
        message = message[3:]
        print "message", message

    print "to_phone_number", to_phone_number
    translated_message = translates(to_phone_number, message)

    print "translated_message, line 65", translated_message

    print from_phone_number
    print MY_PHONE_NUMBER

    # if its from mom or dad, add that its from them in the message
    if from_phone_number != MY_PHONE_NUMBER[1:]:
        translated_message = "{}: {}".format(FROM_PARENTS[from_phone_number].upper(), translated_message.encode('utf-8'))
        print "got into if statment"
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
