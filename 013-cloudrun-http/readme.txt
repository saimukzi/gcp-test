!!! JUST NOTE ONLY !!!

https://console.cloud.google.com/artifacts/docker
https://console.cloud.google.com/run

### Deploy

gcloud artifacts repositories create \
  test-repo-${TTIMESTAMP} \
  --repository-format=docker \
  --location=${GCP_REGION}
  
gcloud builds submit \
  --tag ${GCP_REGION}-docker.pkg.dev/${GCP_PROJECT}/test-repo-${TTIMESTAMP}/test-tag-${TTIMESTAMP} \
  code

gcloud run deploy \
  test-run-013-cloudrun-http-${TTIMESTAMP} \
  --image ${GCP_REGION}-docker.pkg.dev/${GCP_PROJECT}/test-repo-${TTIMESTAMP}/test-tag-${TTIMESTAMP} \
  --region=${GCP_REGION} \
  --allow-unauthenticated

### Remove

gcloud run services delete \
  test-run-013-cloudrun-http-${TTIMESTAMP} \
  --region=${GCP_REGION} \
  --quiet

gcloud artifacts repositories delete \
  test-repo-${TTIMESTAMP} \
  --location=${GCP_REGION} \
  --quiet
