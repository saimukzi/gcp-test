#!/bin/bash -e

. $( cd -- "$( dirname -- "${BASH_SOURCE[0]}" )" &> /dev/null && pwd )/_config.sh
SCRIPT_DIR=$( cd -- "$( dirname -- "${BASH_SOURCE[0]}" )" &> /dev/null && pwd )

gcloud functions deploy ${FUNCTION_NAME_0} \
    --gen2 \
    --memory=128Mi \
    --runtime=python311 \
    --region=${GCP_REGION} \
    --source=${SCRIPT_DIR}/code0 \
    --entry-point=gcp_call \
    --trigger-http \
    --allow-unauthenticated \
    --set-env-vars=GOOGLE_CLOUD_PROJECT=${GCP_PROJECT}

gcloud functions deploy ${FUNCTION_NAME_1} \
    --gen2 \
    --memory=128Mi \
    --runtime=python311 \
    --region=${GCP_REGION} \
    --source=${SCRIPT_DIR}/code1 \
    --entry-point=gcp_call \
    --trigger-topic=${TOPIC_NAME}
