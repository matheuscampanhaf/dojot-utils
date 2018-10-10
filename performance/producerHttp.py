import json
import time
import sys
import requests
import base64


class token_generator:

    userinfo = {
        "username": "internal",
        "service": "admin"
    }

    jwt = "{}.{}.{}".format(base64.b64encode("model".encode()).decode(),
                            base64.b64encode(json.dumps(
                                userinfo).encode()).decode(),
                            base64.b64encode("signature".encode()).decode())

    def get_token(self):
        return self.jwt


def send_requests(num_requests, count):

    token = token_generator()
    jwt = token.get_token()
    data = {
        "label": "",
        "templates": [1],
    }
    start_requests = time.time()
    for i in range(num_requests):
        count += 1
        data["label"] = str(count)
        url = 'http://172.20.0.23:5000/device'
        requests.post(url, headers={
            'Authorization': jwt, 'Content-Type': 'application/json'}, data=json.dumps(data))

    print("Sent %s requests to %s in %s seconds" % (num_requests, url, time.time()-start_requests))


if __name__ == "__main__":

    num_requests = int(sys.argv[1])
    freq = int(sys.argv[2])
    duration = int(sys.argv[3])
    seq_messages = 0

    start = time.time()
    while(time.time() - start <= duration * 60):
        send_requests(num_requests, seq_messages * num_requests)
        seq_messages += 1
        time.sleep(freq)
