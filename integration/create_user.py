import requests
import json
import names
from urllib.error import HTTPError


def post_create_user(full_name, passcode, email, login_type):
    url = "https://drj335kkci.execute-api.sa-east-1.amazonaws.com/dev/v1/users"
    payload = json.dumps({
        "fullName": full_name,
        "password": passcode,
        "email": email,
        "loginType": login_type
    })
    headers = {
        'Content-Type': 'application/json'
    }
    print(payload)
    try:
        response = requests.post(url, headers=headers, data=payload)
    except HTTPError:
        response = requests.post(url, headers=headers, data=payload)

    if response.status_code != 200:
        print("Status code: " + str(response.status_code))
        object_json = json.loads(response.content)
        print(object_json['error']['code'])
        print(object_json['error']['message'])
        return 400

    if response.status_code == 200:
        object_json = json.loads(response.content)
        user = object_json['user']['_id']
        token = object_json["token"]
    return user, token


def get_email():
    first_name = names.get_first_name()
    last_name = names.get_last_name()
    full_name = first_name + " " + last_name
    email = first_name + "_" + last_name + "@gmail.com"
    return full_name, email


''' Step 1 - Create user already exists '''
status_code = post_create_user('Hewerthon Souza', "12345", 'hewerthon@outlook.com', "email")
if status_code == 400:
    print("User already exists")

''' Step 2 - Create user invalid email '''
status_code = post_create_user('Hewerthon Souza', "12345", 'hewerthon.com', "email")
if status_code == 400:
    print("Invalid email ")

''' Step 3 - Create new user '''
full_name, email = get_email()
user, token = post_create_user(full_name, "12345", email, "email")
print("ID user: " + str(user))
print("Token user: " + str(token))


