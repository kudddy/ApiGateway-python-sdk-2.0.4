# coding=utf-8
import requests
from apig_sdk import signer
from json import dumps, loads
from random import choice


phase = ["хочу bmw 3 в москве от 2015 года до 2018"]

if __name__ == '__main__':
    sig = signer.Signer()
    sig.Key = "*"
    sig.Secret = "*"

    body = {'MESSAGE_NAME': 'GET_DUCKLING_RESULT', 'data': {'text': [{'text': 'tesla', 'raw_text': 'tesla', 'grammem_info': {'raw_gram_info': '', 'part_of_speech': 'X'}, 'lemma': 'tesla', 'is_stop_word': False, 'list_of_dependents': [], 'dependency_type': 'case', 'head': 3}, {'text': '2021', 'raw_text': '2021', 'lemma': '2021', 'original_text': 'две тысячи двадцать первого', 'token_type': 'NUM_TOKEN', 'token_value': {'value': 2021, 'adjectival_number': True}, 'list_of_token_types_data': [{'token_type': 'NUM_TOKEN', 'token_value': {'value': 2021, 'adjectival_number': True}}], 'grammem_info': {'numform': 'digit', 'raw_gram_info': 'numform=digit', 'part_of_speech': 'NUM'}, 'is_stop_word': False, 'list_of_dependents': [], 'dependency_type': 'nummod', 'head': 3, 'is_beginning_of_composite': True, 'composite_token_type': 'TIME_DATE_TOKEN', 'composite_token_length': 2, 'composite_token_value': {'year': 2021}}, {'text': 'года', 'raw_text': 'года', 'grammem_info': {'animacy': 'inan', 'case': 'gen', 'gender': 'masc', 'number': 'sing', 'raw_gram_info': 'animacy=inan|case=gen|gender=masc|number=sing', 'part_of_speech': 'NOUN'}, 'lemma': 'год', 'is_stop_word': False, 'list_of_dependents': [1, 2], 'dependency_type': 'root', 'head': 0, 'is_beginning_of_composite': False, 'composite_token_type': 'TIME_DATE_TOKEN', 'composite_token_length': 2, 'composite_token_value': {'year': 2021}}, {'raw_text': '.', 'text': '.', 'lemma': '.', 'token_type': 'SENTENCE_ENDPOINT_TOKEN', 'token_value': {'value': '.'}, 'list_of_token_types_data': [{'token_type': 'SENTENCE_ENDPOINT_TOKEN', 'token_value': {'value': '.'}}]}]}}

    real_body = dumps(body)

    r = signer.HttpRequest("POST",
                           "https://smapi.pv-api.sbc.space/fn_a051b883_f8fd_4a33_b839_66f609f5998f",
                           {"Content-Type": "application/json", "x-stage": "RELEASE"},
                           body=dumps(body))
    sig.Sign(r)
    print(r.headers["X-Sdk-Date"])
    print(r.headers["Authorization"])
    print(r.headers)

    resp = requests.request(r.method, r.scheme + "://" + r.host + r.uri, headers=r.headers, data=r.body, verify=False)

    print(resp.status_code, resp.reason)
    print(resp.content)

    print(loads(resp.content))

