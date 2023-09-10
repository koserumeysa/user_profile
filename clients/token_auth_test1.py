import requests
from pprint import pprint

#{'key': 'eba1d2f3cd47dc01cd058c81dc88ed231d8798e6'}
def client():
    token = 'Token eba1d2f3cd47dc01cd058c81dc88ed231d8798e6'
    headers = {
        'Authorization': token
    }
    response = requests.get(
        url = 'http://127.0.0.1:8000/api/user-profiles/',
        headers=headers,
    )

    print('Status Code: ', response.status_code)

    response_data = response.json()
    pprint(response_data)

#If I run this file in terminal, it will run client().
if __name__ == '__main__':
    client()