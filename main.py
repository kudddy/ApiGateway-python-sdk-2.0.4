# coding=utf-8
import requests
from apig_sdk import signer
from json import dumps, loads

phase = ["хочу bmw 3 в москве от 2015 года до 2018"]

if __name__ == "__main__":
    sig = signer.Signer()
    sig.Key = ""
    sig.Secret = ""

    body = {"MESSAGE_NAME": "GET_DUCKLING_RESULT", "data": {"text": [{"text": "volkswagen", "raw_text": "volkswagen", "grammem_info": {"raw_gram_info": "", "part_of_speech": "X"}, "lemma": "volkswagen", "is_stop_word": False, "list_of_dependents": [2], "dependency_type": "root", "head": 0}, {"text": "crafter", "raw_text": "crafter", "grammem_info": {"raw_gram_info": "", "part_of_speech": "X"}, "lemma": "crafter", "is_stop_word": False, "list_of_dependents": [], "dependency_type": "flat:foreign", "head": 1}, {"raw_text": ".", "text": ".", "lemma": ".", "token_type": "SENTENCE_ENDPOINT_TOKEN", "token_value": {"value": "."}, "list_of_token_types_data": [{"token_type": "SENTENCE_ENDPOINT_TOKEN", "token_value": {"value": "."}}]}]}}

    real_body = dumps(body)

    r = signer.HttpRequest("POST",
                           "https://smapi.pv-api.sbc.space/fn_bab940f4_a4ce_4c1a_81b3_d807e34d7e3f",
                           {"Content-Type": "application/json", "x-stage": "RELEASE"},
                           body=dumps(body))
    sig.Sign(r)

    resp = requests.request(r.method, r.scheme + "://" + r.host + r.uri, headers=r.headers, data=r.body, verify=False)

    print(resp.status_code, resp.reason)
    print(resp.content)

    print(loads(resp.content))
