import functions_framework
import json
import time

# request: https://flask.palletsprojects.com/en/2.3.x/api/#incoming-request-data
def main(method, args, data, **kwargs):
    now = time.time()
    print(json.dumps({
        'severity': 'DEBUG',
        'message': f'now={now}, method={method}, args={args}, data={data}',
        'logging.googleapis.com/labels': {
            'function_name': '010-functions-http'
        }
    }))
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
