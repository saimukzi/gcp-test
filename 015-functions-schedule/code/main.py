import base64
import datetime
import json
import time

def main(data, message_id, publish_time, **kwargs):
    now = time.time()
    print(json.dumps({
        'severity': 'DEBUG',
        'message': f'now={now}, data={data}, message_id={message_id}, publish_time={publish_time}'
    }))
    return "Hello World!"

def gcp_call(event, context):
    data = base64.b64decode(event['data']).decode('utf-8')
    message_id = event['message_id']
    # publish_time = event['publish_time']
    publish_time = datetime.datetime.strptime(event['publish_time'], '%Y-%m-%dT%H:%M:%S.%fZ')
    publish_time = publish_time.replace(tzinfo=datetime.timezone.utc)
    return main(data, message_id, publish_time, event=event, context=context)

if __name__ == '__main__':
    import argparse

    parser = argparse.ArgumentParser()
    parser.add_argument('--data', type=str, default='test')
    parser.add_argument('--message_id', type=str, default=None)
    args = parser.parse_args()

    publish_time = datetime.datetime.utcnow().replace(tzinfo=datetime.timezone.utc)

    data = args.data
    message_id = args.message_id
    if message_id is None:
        message_id = str(int(publish_time.timestamp() * 1000))

    main(data, message_id, publish_time)
