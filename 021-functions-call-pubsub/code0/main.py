import functions_framework
import google.cloud.pubsub_v1
import json
import os
import time

# request: https://flask.palletsprojects.com/en/2.3.x/api/#incoming-request-data
def main(method, args, data, **kwargs):
    now = time.time()
    print(json.dumps({
        'severity': 'DEBUG',
        'message': f'now={now}, method={method}, args={args}, data={data}',
    }))

    publisher = google.cloud.pubsub_v1.PublisherClient()
    topic_name = 'projects/{project_id}/topics/{topic}'.format(
        project_id=os.getenv('GOOGLE_CLOUD_PROJECT'),
        topic='smz-gcp-021-functions-call-pubsub-topic',
    )
    print(json.dumps({
        'severity': 'DEBUG',
        'message': f'topic_name={topic_name}',
    }))
    publisher.publish(topic_name, b'YFLWSTMBZM') # fire and forget
    return "Hello World!"

@functions_framework.http
def gcp_call(request):
    method = request.method
    args = request.args
    data = request.data
    return main(method, args, data, request=request)

if __name__ == '__main__':
    import argparse
    import json

    parser = argparse.ArgumentParser()
    parser.add_argument('--method', type=str, default='GET')
    parser.add_argument('--args', type=str, default='{}')
    parser.add_argument('--data', type=str, default='')
    args = parser.parse_args()

    aargs = json.loads(args.args)
    ddata = args.data.encode('utf-8')

    main(args.method, aargs, ddata)
