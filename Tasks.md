### Create Repo
~~1. Create repo on github~~

### Create service using FastAPI
~~1. Create service using FASTAPI~~
~~2. Host service locally and test~~

### Add service into Docker Image
~~1. Add Dockerfile and add container instructions~~
~~2. Test Docker image~~

### Add subscribe feature
~~1. Add endpoints to subscribe and unsubscribe~~
~~2. Add new db connection~~
~~3. Add basemodels~~
~~4. Refactor existing code~~
5. Add testing

### Add unsubscribe feature
~~1. Add new endpoint to unsubscribe~~
~~2. Add new subscribe_repo def~~
~~3. Test it manually~~
4. Write unit tests

### Add recipe db
1. Design

### Formulate idea
1. Online personal recipe diary
2. Plugins to add nutrional charts
3. Online recipe book

### Pipeline
1. Investigate pipelines and repos in GCP

### Design API
1. Design endpoints and service.
   2. subscriber - add subscriber and remove subscriber
   3. recipe book - add recipe book, fetch my recipe books, delete my empty recipe book, search my books
   4. recipes - add new recipe and linked to a recipe book name, view my recipes, search my recipes
   5. login - create a user with password and add them to subscribers
   6. cookbook library - add a shelf?
   7. nutrition - calculate nutrition for my recipe
   8. meal plan - create a meal plan
2. Investigate Rapid API for free recipe apis

### Data Storage
~~1. Investigate storage options on gcp - too expensive, using cockroachdb for free~~
~~2. Investigate how to connect and create db storage (https://www.cockroachlabs.com/docs/stable/connect-to-the-database?filters=python&filters=psycopg3)~~
3. Design database - Subscriber table added.

### Frontend
1. Set up NextJS project for UI

### Create recipe data
1. Design recipe data and labelling
2. Think about grocery list

### Search for recipe by ingredients
1. Create free text search by ingredients

### Upload your rezzipea
1. User upload experience

### Google SEO

### Domain rental
1. Get a domain only for the frontend.

------------
Summary

NEXT
- Test new subscription endpoints with unit tests
- How to deploy my container to GCP (manually trigger and hosting)
- Add DB connection string on safe env variable on GCP and read it from there.
- Create a UI to join the waiting list - BIG!

COMPLETED/LEARNED
- Connected to DB and tested locally
- Added DOCKER ENV variables with db connections safely
- Connect to cockroach db - similar to any postgres db
- Added certs to ~/.postgres
- Tested on docker.
- Add write to DB to update subscriber list
- Added logging
- Test subscribe feature manually
- Added unsubscribe
- Test unsubscribe manually
- Synced repo with Google build and set up a manual trigger
- You need to expose a port outside the container - added EXPOSE to the docker file
- Tested new features with Docker, issues with pathing - I need to use relative paths here and not absolute
- Added isort to venv - run `isort *` to clean imports.
