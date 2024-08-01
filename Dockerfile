FROM --platform=linux/amd64 amopromo/python3.9-nginx

# Set PYTHONPATH to include the /code directory
ENV PYTHONPATH=/code
# create a working directory inside the docker image
WORKDIR /code

# Create directory if it doesn't exist
RUN mkdir -p ~/.postgresql

# Copy the PostgreSQL root certificate file into the Docker image
COPY postgresql/docker/root.crt ~/.postgresql/

RUN pip3 install --no-cache-dir --upgrade pip

# move the requirements file from the root directory in the rezzipea_service to the code directory inside the docker image
COPY requirements.txt /code/requirements.txt

RUN pip3 install --no-cache-dir --upgrade -r /code/requirements.txt

# Move the code from the app folder to insider the docker container under /code/app
COPY ./app /code/app

# Expose the port
EXPOSE 8080

# Define environment variable
ENV PORT=8080

# run the uvicorn server
CMD ["gunicorn", "-w", "4", "-k", "uvicorn.workers.UvicornWorker", "app.handlers.main:app", "--host", "0.0.0.0", "--port", "8080","--timeout-keep-alive", "600"]
