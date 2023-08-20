import json
import os
# import time

IS_GCP = 'GAE_RUNTIME' in os.environ

if IS_GCP:
    import functions_framework
    import google.cloud.client

# request: https://flask.palletsprojects.com/en/2.3.x/api/#incoming-request-data
def main(method, args, data, **kwargs):
    ENV_DICT = {}
    for name, value in os.environ.items():
        ENV_DICT[name] = value
    client_dict = {}
    if IS_GCP:
        client = google.cloud.client.ClientWithProject()
        client_dict['project'] = client.project
    print(json.dumps({
        'severity': 'DEBUG',
        'message': f'ENV_DICT={ENV_DICT}, client_dict={client_dict}',
    }))
    return json.dumps({'ENV_DICT': ENV_DICT, 'client_dict': client_dict})

if IS_GCP:
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
