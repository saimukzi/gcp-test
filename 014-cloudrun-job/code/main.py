import json
import time

if __name__ == "__main__":
    now = time.time()
    print(json.dumps({
        'severity': 'DEBUG',
        'message': f'now={now}',
        'logging.googleapis.com/labels': {
            'test_label_UNASJVHLBU': 'test-value-VIHFHNABIY'
        }
    }))
    # print('HelloWorld ZWWKKGHLJQ!!!')
