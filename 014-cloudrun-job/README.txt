# https://console.cloud.google.com/artifacts
# https://console.cloud.google.com/run

TTIMESTAMP=$(date +%s)

gcloud artifacts repositories create \
  test-014-${TTIMESTAMP}-repo \
  --repository-format=docker \
  --location=${GCP_REGION}

gcloud artifacts repositories list \
  --location=${GCP_REGION}

gcloud builds submit \
  --pack image=${GCP_REGION}-docker.pkg.dev/${GCP_PROJECT}/test-014-${TTIMESTAMP}-repo/test-014-${TTIMESTAMP}-image \
  code

gcloud artifacts files list \
  --location=${GCP_REGION} \
  --repository=test-014-${TTIMESTAMP}-repo

gcloud run jobs create test-014-${TTIMESTAMP}-job \
  --image ${GCP_REGION}-docker.pkg.dev/${GCP_PROJECT}/test-014-${TTIMESTAMP}-repo/test-014-${TTIMESTAMP}-image \
  --max-retries 5 \
  --region ${GCP_REGION} \
  --project=${GCP_PROJECT}

gcloud run jobs list \
  --region ${GCP_REGION} \
  --project=${GCP_PROJECT}

gcloud run jobs execute test-014-${TTIMESTAMP}-job

gcloud run jobs executions list \
  --job=test-014-${TTIMESTAMP}-job \
  --region ${GCP_REGION} \
  --project=${GCP_PROJECT}

gcloud scheduler jobs create http \
  test-014-${TTIMESTAMP}-scheduler \
  --schedule="* * * * *" \
  --uri="https://${GCP_REGION}-run.googleapis.com/apis/run.googleapis.com/v1/namespaces/${GCP_PROJECT}/jobs/test-014-${TTIMESTAMP}-job:run" \
  --oauth-service-account-email=${GCP_SERVICE_ACCOUNT_EMAIL} \
  --oauth-token-scope=https://www.googleapis.com/auth/cloud-platform \
  --location ${GCP_REGION} \
  --project=${GCP_PROJECT}

gcloud scheduler jobs list \
  --location=${GCP_REGION} \
  --project=${GCP_PROJECT}

gcloud scheduler jobs delete \
  test-014-${TTIMESTAMP}-scheduler \
  --location=${GCP_REGION} \
  --project=${GCP_PROJECT} \
  --quiet

# may fail because there is job running
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
