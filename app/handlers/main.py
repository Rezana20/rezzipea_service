import os
import re
import logging
import sys
from typing import Dict

from fastapi import FastAPI, HTTPException

# Ensure the app module is in the path
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from rezzipea_service.app.db.subscriber_repository import SubscriberRepository
from rezzipea_service.app.models.subcriber_models import SubscriberRequest

logger = logging.getLogger(__name__)
logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')

app = FastAPI()


@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.post("/newsletter/subscribe")
def newsletter_subscribe(request: SubscriberRequest) -> Dict[str, str]:
    logger.info('newsletter_subscribe')

    email_address_pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    if not re.match(email_address_pattern, request.email_address):
        logger.warning(f'Invalid email address format: {request.email_address}')
        raise HTTPException(status_code=400, detail=f"Invalid email address: {request.email_address}")
    logger.info('Validated email format successfully')

    subscriber = SubscriberRepository()
    if not subscriber.add_subscriber(request.email_address, request.user_name):
        logger.warning(f'Unable to add subscriber: {request.email_address}')
        raise HTTPException(status_code=409, detail=f"Unable to add subscriber: {request.email_address}")
    else:
        return {"status": "success", "message": "Subscribed with {0}".format(request.email_address)}


@app.post("/newsletter/unsubscribe")
def newsletter_subscribe(email_address: str):
    subscriber = SubscriberRepository()
    if subscriber.remove_subscriber(email_address):
        return {"status": "success", "message": "Feature in progress, we will remove {0} soon".format(email_address)}

