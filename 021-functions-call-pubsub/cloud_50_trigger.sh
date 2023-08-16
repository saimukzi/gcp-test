#!/bin/bash -e

. $( cd -- "$( dirname -- "${BASH_SOURCE[0]}" )" &> /dev/null && pwd )/_config.sh

URL=$(gcloud functions describe ${FUNCTION_NAME_0} \
    --gen2 \
    --region=${GCP_REGION} \
    --format="value(serviceConfig.uri)")

echo "URL: ${URL}"

# curl -X POST \
#     -H "Content-Type:application/json" \
#     -d "{\"project_id\":\"${GCP_PROJECT}\"}" \
#      ${URL}
curl ${URL}

echo ""
