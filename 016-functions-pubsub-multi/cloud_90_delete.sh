#!/bin/bash -e

. $( cd -- "$( dirname -- "${BASH_SOURCE[0]}" )" &> /dev/null && pwd )/_config.sh

gcloud functions delete ${FUNCTION_NAME_0} \
    --gen2 \
    --region=${GCP_REGION} \
    --quiet

gcloud functions delete ${FUNCTION_NAME_1} \
    --gen2 \
    --region=${GCP_REGION} \
    --quiet
