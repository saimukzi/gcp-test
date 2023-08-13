#!/bin/bash -e

. $( cd -- "$( dirname -- "${BASH_SOURCE[0]}" )" &> /dev/null && pwd )/_config.sh
SCRIPT_DIR=$( cd -- "$( dirname -- "${BASH_SOURCE[0]}" )" &> /dev/null && pwd )

gcloud functions deploy ${FUNCTION_NAME} \
    --gen2 \
    --memory=128Mi \
    --runtime=python311 \
    --region=${GCP_REGION} \
    --source=${SCRIPT_DIR}/code \
    --entry-point=gcp_call \
    --trigger-topic=${TOPIC_NAME}
