#!/bin/bash -e

. $( cd -- "$( dirname -- "${BASH_SOURCE[0]}" )" &> /dev/null && pwd )/_config.sh
#SCRIPT_DIR=$( cd -- "$( dirname -- "${BASH_SOURCE[0]}" )" &> /dev/null && pwd )

URL=$(gcloud functions describe ${FUNCTION_NAME} \
    --gen2 \
    --region=${GCP_REGION} \
    --format="value(serviceConfig.uri)")

echo "URL: ${URL}"

curl ${URL}

echo ""
