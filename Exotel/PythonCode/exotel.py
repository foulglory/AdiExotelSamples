# Send an SMS in response to an SMS/ persist details of an SMS in the DB

from pprint import pprint
import requests

from settings import sid, token

	
def send_message(sid, token, sms_from, sms_to, sms_body):
    return requests.post('https://twilix.exotel.in/v1/Accounts/{sid}/Sms/send.json'.format(sid=sid),
        auth=(sid, token),
        data={
            'From': sms_from,
            'To': sms_to,
            'Body': sms_body
        })

if __name__ == '__main__':
		sms_from = self.request.get('From')
		sms_to = self.request.get('To')
		r = send_message(sid, token,
        sms_from ,#sms_from='8808891988',  # sms_from='8808891988',
        sms_to ,#sms_to='9741948540', # sms_to='9052161119',
        sms_body='Your regsitration for CFG has been confirmed')



# GET
#r = requests.get(url)

# GET with params in URL
#r = requests.get(url, params=payload)

# POST with form-encoded data
#r = requests.post(url, data=payload)

# POST with JSON 
import json
#r = requests.post(url, data=json.dumps(payload))

# Response, status etc
#r.text
#r.status_code