# coding=utf-8
import requests
from apig_sdk import signer
from json import dumps, loads
from random import choice


phase = ["хочу bmw 3 в москве до 1994 года"]

if __name__ == '__main__':
    sig = signer.Signer()
    sig.Key = "*"
    sig.Secret = "*"

    body = {
        "MESSAGE_NAME": "GET_DUCKLING_RESULT",
        "data": {
            "text": choice(phase)
        }
    }

    real_body = dumps(body)

    r = signer.HttpRequest("POST",
                           "https://smapi.pv-api.sbc.space/fn_a051b883_f8fd_4a33_b839_66f609f5998f",
                           {"Content-Type": "application/json", "x-stage": "RELEASE"},
                           body=dumps(body))
    sig.Sign(r)

    resp = requests.request(r.method, r.scheme + "://" + r.host + r.uri, headers=r.headers, data=r.body, verify=False)

    print(resp.status_code, resp.reason)

    print(loads(resp.content))

