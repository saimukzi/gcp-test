TTIMESTAMP=$(date +%s)

gcloud artifacts repositories create \
  test-014-${TTIMESTAMP}-repo \
  --repository-format=docker \
  --location=${GCP_REGION}

gcloud builds submit \
  --pack image=${GCP_REGION}-docker.pkg.dev/${GCP_PROJECT}/test-014-${TTIMESTAMP}-repo/test-014-${TTIMESTAMP}-image \
  code

gcloud run jobs create test-014-${TTIMESTAMP}-job \
  --image ${GCP_REGION}-docker.pkg.dev/${GCP_PROJECT}/test-014-${TTIMESTAMP}-repo/test-014-${TTIMESTAMP}-image \
  --max-retries 5 \
  --region ${GCP_REGION} \
  --project=${GCP_PROJECT}

gcloud run jobs execute test-014-${TTIMESTAMP}-job

gcloud run jobs delete test-014-${TTIMESTAMP}-job \
  --region ${GCP_REGION} \
  --project=${GCP_PROJECT} \
  --quiet

gcloud artifacts docker images delete \
  ${GCP_REGION}-docker.pkg.dev/${GCP_PROJECT}/test-014-${TTIMESTAMP}-repo/test-014-${TTIMESTAMP}-image \
  --quiet

gcloud artifacts repositories delete \
  test-014-${TTIMESTAMP}-repo \
  --location=${GCP_REGION} \
  --quiet
