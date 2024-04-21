import csv
import re
import logging

from fastapi import FastAPI

from app.db.cockroach_db import CockroachDBConnection

logger = logging.getLogger(__name__)

app = FastAPI()

@app.get("/")
def read_root():
    return {"Hello": "World"}

@app.post("/newsletter/subscribe")
def newsletter_subscribe(user_name: str, email_address: str):
    logger.info("This is a log message from your endpoint")
    # validate email address
    email_address_pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    if not re.match(email_address_pattern, email_address):
        return {"status": "failure", "message": "Invalid email address {0}".format(email_address)}

    db = CockroachDBConnection()
    if db.is_subscriber_email_unique(email_address):
        # TODO add email address
        return {"status": "success", "message": "Subscribed with {0}".format(email_address)}
    else:
        return {"status": "failure", "message": "Already subscribed with {0}".format(email_address)}


@app.post("/newsletter/unsubscribe")
def newsletter_subscribe(email: str):
    with open("app/data/subscribers.csv", 'r', newline='') as infile, open("app/data/subscribers.csv", 'w',
                                                                      newline='') as outfile:
        reader = csv.reader(infile)
        writer = csv.writer(outfile)

        # Iterate through each row in the input file
        for row in reader:
            # Check if the email address in the row matches the one to delete
            # row[0] is name and row[1] is user email address
            if email == row[1]:
                # Skip this row if the email matches
                continue
            # Write the row to the output file if the email doesn't match
            writer.writerow(row)

    return {"status": "success", "message": "We are sorry to see you leave."
                                            " Unsubscribed from our content, from {0}".format(email)}
