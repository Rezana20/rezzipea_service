import csv
from typing import Union

from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def read_root():
    return {"Hello": "World"}

@app.post("/newsletter/subscribe")
def newsletter_subscribe(user_name: str, email: str):
    csv_writer = csv.writer(open("../data/subscribers"))
    csv_writer.writerow([user_name, email])

    return {"status": "success", "message": "Subscribed with {0}".format(email)}


@app.post("/newsletter/unsubscribe")
def newsletter_subscribe(email: str):
    with open("../data/subscribers", 'r', newline='') as infile, open("../data/subscribers", 'w',
                                                                      newline='') as outfile:
        reader = csv.reader(infile)
        writer = csv.writer(outfile)

        # Iterate through each row in the input file
        for row in reader:
            # Check if the email address in the row matches the one to delete
            if email == row[email_address]:
                # Skip this row if the email matches
                continue
            # Write the row to the output file if the email doesn't match
            writer.writerow(row)

    return {"status": "success", "message": "We are sorry to see you leave."
                                            " Unsubscribed from our content, from {0}".format(email)}
