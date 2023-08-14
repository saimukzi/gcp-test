#!/bin/bash -e

. $( cd -- "$( dirname -- "${BASH_SOURCE[0]}" )" &> /dev/null && pwd )/_config.sh

gcloud pubsub topics delete ${TOPIC_NAME}
