import json
import os
import requests

from pprint import pprint


key = os.environ["MAILGUN_API_KEY"]

def send_mail(to, subject, html):

    request_url = "https://api.mailgun.net/v3/sandbox8d49438756d044e9aa163301ea74151c.mailgun.org/messages"
    data = {
        'from': 'noreply@sandbox8d49438756d044e9aa163301ea74151c.mailgun.org',
        'to': to,
        'subject': subject,
        'html': html
    }

    print("before post")
    request = requests.post(request_url, auth=('api', key), data=data)

    print("after post")
    request_json = request.json()

    pprint(json.dumps(request_json))

if __name__ == "__main__":
    send_mail('jackkitte735@gmail.com', 'Test Message', 'Hello Everyone!')
