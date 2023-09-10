import requests
from pprint import pprint

#{'key': 'eba1d2f3cd47dc01cd058c81dc88ed231d8798e6'}
def client():
    credentials = {
        'username': 'final_user',
        'password': 'test321..'
    }

    response = requests.get(
        url = 'http://127.0.0.1:8000/api/rest-auth/login/',
        data=credentials,
    )

    print('Status Code: ', response.status_code)

    response_data = response.json()
    pprint(response_data)

#If I run this file in terminal, it will run client().
if __name__ == '__main__':
    client()