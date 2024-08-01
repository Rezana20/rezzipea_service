# rezzipea_service
This is a website for my recipes

### Coding rules
1. Run `isort *` before commiting to github
2. Run `black` before commiting to github

### Run the service locally
Go to one level above rezzipea_service
```bash
    python3 -m venv rezzipeas_venv
    source /Users/rezanadowra/Documents/GitHub/rezzipea_service/rezzipeas_venv/bin/activate
    uvicorn app.handlers.main:app --host 0.0.0.0 --port 80
```
Hint you should see that you are in the virtual env on your terminal

This service has FastAPI docs. You can navigate to `http://127.0.0.1/docs` to use the api.

To deactivate the python env run `deactivate`

### Manage the database
Console view:
- Navigate to https://cockroachlabs.cloud/cluster/3250ce6a-65af-4039-a737-1631378f5a0d/overview

Connection steps:
- https://www.cockroachlabs.com/docs/stable/connect-to-the-database?filters=python&filters=psycopg3

### Run the service in a docker container
1. Start docker
2. Delete old containers + images
3. Run `docker build -t myimage .  ` to create the image
4. Run image in my container with ` docker run -d --name mycontainer -p 80:80 --env-file dev.env  myimage`
5. Navigate to `http://0.0.0.0:80` or `http://127.0.0.1/docs `

### Setup

If you wish to install a Python library that isn't in Homebrew, use a virtual environment:

python3 -m venv rezzipeas_venv
source /Users/dowra/Documents/GitHub/rezzipea_service/rezzipeas_venv/bin/activate
python3 -m pip install <package-name>

#### Troubleshooting

1. I tried using the env and I when running the uvicorn command I get uvicorn not found.
   - python3 -m uvicorn app.handlers.main:app --reload

### Links

- Initial Setup was inspired from https://fastapi.tiangolo.com/deployment/docker/
