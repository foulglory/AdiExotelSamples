#!/usr/bin/env python
# -*- coding: utf-8 -*-

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

    r = send_message(sid, token,
        sms_from='9243422233',  # sms_from='8808891988',
        sms_to=['7760094314'], # sms_to='9052161119',
        sms_body='Your regsitration for CFG has been confirmed')
    print(r.status_code)
    pprint(r.json())
