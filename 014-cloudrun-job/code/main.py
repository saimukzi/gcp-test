import json
import os
import time

IS_GCP = 'CLOUD_RUN_JOB' in os.environ

if IS_GCP:
    import google.cloud.client

if __name__ == "__main__":
    now = time.time()

    print(json.dumps({
        'severity': 'DEBUG',
        'message': f'now={now}',
        'logging.googleapis.com/labels': {
            'test_label_UNASJVHLBU': 'test-value-VIHFHNABIY'
        }
    }))

    ENV_DICT = {}
    for name, value in os.environ.items():
        ENV_DICT[name] = value
    print(json.dumps({
        'severity': 'DEBUG',
        'message': f'ENV_DICT={ENV_DICT}',
    }))

    if IS_GCP:
        client = google.cloud.client.ClientWithProject()
        client_project = client.project
        print(json.dumps({
            'severity': 'DEBUG',
            'message': f'client_project={client_project}',
        }))

    # print('HelloWorld ZWWKKGHLJQ!!!')
