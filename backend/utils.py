import re
import hashlib


def md5(msg='', mix=''):
    MD5 = hashlib.md5()
    MD5.update(msg.encode('utf-8', 'ignore'))
    msg2 = MD5.hexdigest()
    msg2 = msg2[3:-3][5:] + mix
    MD5.update(msg2.encode('utf-8', 'ignore'))
    return MD5.hexdigest()

def is_email(text):
    pattern = r'^([a-zA-Z0-9_\-\.]+)@((\[[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.)|(([a-zA-Z0-9\-]+\.)+))([a-zA-Z]{1,5}|[0-9]{1,3})(\]?)$'
    return bool(re.match(pattern, text))

def is_phone(text):
    pattern = r'^[1][3,4,5,7,8][0-9]{9}$'
    return bool(re.match(pattern, text))