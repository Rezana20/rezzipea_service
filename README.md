# rezzipea_service
This is a website for my recipes

### Run the service locally
```bash
    python3 -m venv rezzipeas_venv
    source /Users/dowra/Documents/GitHub/rezzipea_service/rezzipeas_venv/bin/activate
    
    uvicorn app.handlers.main:app --host 0.0.0.0 --port 80  
```
This service has FastAPI docs. You can navigate to `http://127.0.0.1/docs` to use the api.

### Run the service in a docker container
1. Start docker
2. Delete old containers + images
3. Run `docker build -t myimage .  ` to create the image 
4. Run image in my container with `docker run -d --name mycontainer -p 80:80 myimage `
5. Navigate to `http://0.0.0.0:80` or `http://127.0.0.1/docs`

### Setup 

If you wish to install a Python library that isn't in Homebrew, use a virtual environment:

python3 -m venv rezzipeas_venv
source /Users/dowra/Documents/GitHub/rezzipea_service/rezzipeas_venv/bin/activate
python3 -m pip install <package-name>


### Links

- Initial Setup was inspired from https://fastapi.tiangolo.com/deployment/docker/

