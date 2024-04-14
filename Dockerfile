FROM amopromo/python3.9-nginx

# create a working directory inside the docker image
WORKDIR /code

# move the requirements file from the root directory in the rezzipea_service to the code directory inside the docker image
COPY requirements.txt /code/requirements.txt

RUN pip install --no-cache-dir --upgrade -r /code/requirements.txt

# Move the code from the app folder to insider the docker container under /code/app
COPY ./app /code/app

# run the uvicorn server
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "80"]

