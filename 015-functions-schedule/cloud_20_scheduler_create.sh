#!/bin/bash -e

. $( cd -- "$( dirname -- "${BASH_SOURCE[0]}" )" &> /dev/null && pwd )/_config.sh

gcloud scheduler jobs create pubsub ${SCHEDULER_JOB_NAME} \
  --location ${GCP_REGION} \
  --schedule "*/1 * * * *" \
  --topic ${TOPIC_NAME} \
  --message-body "Message body $(date +%s)" \
  --time-zone "${GCP_TIMEZONE}"
