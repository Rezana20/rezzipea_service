#!/bin/bash

# Exit immediately if a command exits with a non-zero status
set -e

# Set project variables
export GCLOUD_PROJECT="maihem"
export REPO="maihem-api"
export REGION="europe-west2"
export IMAGE="rez-maihem-api-image"

# Log in to Google Cloud
#gcloud auth login

# Set the project
gcloud config set project $GCLOUD_PROJECT

# Verify if the user has the necessary permissions
echo "Verifying permissions for user: $(gcloud config get-value account)"
if ! gcloud projects get-iam-policy $GCLOUD_PROJECT --flatten="bindings[].members" --format="table(bindings.role)" --filter="bindings.members:$(gcloud config get-value account)" | grep -q "roles/artifactregistry.admin"; then
  echo "Error: The current user does not have the Artifact Registry Administrator role. Please add the role and try again."
  exit 1
fi

# Enable required services
gcloud services enable artifactregistry.googleapis.com run.googleapis.com

# Check if the Artifact Registry repository exists
if ! gcloud artifacts repositories describe $REPO --location=$REGION &> /dev/null; then
  # Create Artifact Registry repository if it doesn't exist
  gcloud artifacts repositories create $REPO \
    --repository-format=docker \
    --location=$REGION \
    --description="Docker repository"
else
  echo "Repository $REPO already exists in region $REGION."
fi

# Construct the image tag URL
export IMAGE_TAG=${REGION}-docker.pkg.dev/$GCLOUD_PROJECT/$REPO/$IMAGE

## Build the Docker image locally
#docker build -t $IMAGE .

# Tag the Docker image for Artifact Registry
docker tag $IMAGE $IMAGE_TAG

## Push the Docker image to Artifact Registry
#docker push $IMAGE_TAG

gcloud builds submit --pack image=$IMAGE_TAG

# Deploy to Cloud Run
gcloud run deploy myfastapiapp  --port 8080 --image $IMAGE_TAG --region $REGION --platform managed
#gcloud run deploy app.yaml --project=$GCLOUD_PROJECT

# Print completion message
echo "Deployment script completed."

#https://myfastapiapp-dot-maihem.nw.r.appspot.com
