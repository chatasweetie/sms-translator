import os

# Family's Phone Numbers
MOM_NUMBER=os.environ.get("MOM_NUMBER")
DAD_NUMBER=os.environ.get("DAD_NUMBER")
JESSICA_NUMBER=os.environ.get("JESSICA_NUMBER")

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
}

PARENTS = {
    "mom" : MOM_NUMBER,
    "dad" : DAD_NUMBER,
}

FROM_PARENTS = {
    MOM_NUMBER : "mom",
    DAD_NUMBER : "dad",
}

MY_PHONE_NUMBER = JESSICA_NUMBER
