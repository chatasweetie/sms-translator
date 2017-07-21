import os

# Family's Phone Numbers
MOM_NUMBER=os.environ.get("MOM_NUMBER")
DAD_NUMBER=os.environ.get("DAD_NUMBER")
JESSICA_NUMBER=os.environ.get("JESSICA_NUMBER")
JAMES_NUMBER=os.environ.get("JAMES_NUMBER")

PHONE_DIRECTORY = {
    JESSICA_NUMBER: {
                    'language': 'en',
                    'name':'Jessica',
                },
    MOM_NUMBER: {
                    'language': 'ko',
                    'name':'Mom',
                },
    DAD_NUMBER: {
                    'language': 'ko',
                    'name':'Dad',
                },
    JAMES_NUMBER: {
                    'language': 'ko',
                    'name':'jam',
                },
}

PARENTS = {
    "mom" : MOM_NUMBER,
    "dad" : DAD_NUMBER,
    "jam" : JAMES_NUMBER,
}

FROM_PARENTS = {
    MOM_NUMBER : "mom",
    DAD_NUMBER : "dad",
    JAMES_NUMBER : "jam"
}

MY_PHONE_NUMBER = JESSICA_NUMBER
