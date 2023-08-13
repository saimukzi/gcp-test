#!/bin/bash -e

. $( cd -- "$( dirname -- "${BASH_SOURCE[0]}" )" &> /dev/null && pwd )/_config.sh

gcloud scheduler jobs delete ${SCHEDULER_JOB_NAME} \
  --location ${GCP_REGION} \
  --quiet
