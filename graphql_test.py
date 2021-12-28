from gql import Client, gql
from gql.transport.requests import RequestsHTTPTransport
import requests.auth
import json

from apig_sdk import signer

dataspace_url = "https://smapi.pv-api.sbc.space/ds-7043743249627480066/graphql"
app_key = ""
app_secret = ""


class DataspaceAuth(requests.auth.AuthBase):
    def __call__(self, r):
        if app_key is None or app_secret is None:
            print("APP_SECRET or APP_KEY is undefined. Request will not be signed")
            return r

        sig = signer.Signer()
        sig.Key = app_key
        sig.Secret = app_secret
        request = signer.HttpRequest(r.method, r.url, r.headers, r.body.decode('utf-8'))
        sig.Sign(request)
        r.headers = request.headers
        return r


# Инициализация GraphQl клиента
if dataspace_url is not None:
    transport = RequestsHTTPTransport(url=dataspace_url, auth=DataspaceAuth(), verify=False)
    client = Client(transport=transport, fetch_schema_from_transport=False)
    graphql_status = "Dataspace URL: " + dataspace_url
else:
    client = None
    graphql_status = "DATASPACE_URL environment variable is not set. GraphQL client disabled"
print(graphql_status)


# Пример вызова DataSpace с подписью
def call_dataspace():
    # Запрос
    query = gql("""query {
  searchLogData{
    elems {
      text,
      sessionId,
      userId,
      time
    }
  }
}""")
    # variable_values = {
    #     "paramId": "paramValue"
    # }
    # Вызов Dataspace
    return client.execute(query)


# print(call_dataspace())

def insert_value_to_audit(user_id: str,
                          session_id: str,
                          text: str):
    query = gql("""mutation ($text: String!, $sessionId: String!, $userId: String!){
  p1: packet {
    createLogData(input: {
      text: $text,
      sessionId: $sessionId,
      userId: $userId
    }){
      text
    }
  }
}""")
    variable_values = {
        "text": text,
        "sessionId": session_id,
        "userId": user_id
    }
    print(variable_values)
    return client.execute(query, variable_values=json.dumps(variable_values))


print(insert_value_to_audit(
    user_id="34r243",
    session_id="fds34-sdfa",
    text="fsdfsdf"
))
