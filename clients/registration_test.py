import requests
from pprint import pprint

# 'key': '0b9c8e4e436dc256447e012f89ca3a495a621289'
def client():
    credentials = {
        'username': 'rest_final_user',
        'email': 'test@test.com',
        'password1': 'test321..',
        'password2': 'test321..',
    }

    response = requests.post(
        url = 'http://127.0.0.1:8000/api/rest-auth/registration/',
        data=credentials,
    )

    print('Status Code: ', response.status_code)

    response_data = response.json()
    pprint(response_data)

#If I run this file in terminal, it will run client().
if __name__ == '__main__':
    client()