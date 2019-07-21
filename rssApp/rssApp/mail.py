import json
import os
import requests

from pprint import pprint


key = os.environ['MAILGUN_API_KEY']

def send_mail(to, subject, html):

    request_url = "https://api.mailgun.net/v3/sandbox8d49438756d044e9aa163301ea74151c.mailgun.org/messages"
    data = {
        'from': 'noreply@sandbox8d49438756d044e9aa163301ea74151c.mailgun.org',
        'to': to,
        'subject': subject,
        'html': html
    }

    request = requests.post(request_url, auth=('api', key), data=data)
    request_json = request.json()
    pprint(json.dumps(request_json))
