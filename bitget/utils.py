import hmac
import base64
import time
import json
import bitget.consts as c


def sign(message, secret_key):
    mac = hmac.new(bytes(secret_key, encoding='utf8'), bytes(message, encoding='utf-8'), digestmod='sha256')
    d = mac.digest()
    return base64.b64encode(d)


def pre_hash(timestamp, method, request_path, body):
    return str(timestamp) + str.upper(method) + request_path + body


def get_header(api_key, sign, timestamp, passphrase):
    header = dict()
    header[c.CONTENT_TYPE] = c.APPLICATION_JSON
    header[c.ACCESS_KEY] = api_key
    header[c.ACCESS_SIGN] = sign
    header[c.ACCESS_TIMESTAMP] = str(timestamp)
    header[c.ACCESS_PASSPHRASE] = passphrase
    return header


def parse_params_to_str(params):
    url = '?'
    for key, value in params.items():
        url = url + str(key) + '=' + str(value) + '&'

    return url[0:-1]


def get_timestamp():
    return int(time.time() * 1000)


def signature(timestamp, method, request_path, body, secret_key):
    if str(body) == '{}' or str(body) == 'None':
        body = ''
    message = pre_hash(timestamp, method, request_path, body)
    return sign(message, secret_key)


if __name__ == '__main__':
    secret_key = 'your_key'
    
    timestamp = get_timestamp()
    method = 'GET'
    request_path = '/api/spot/v1/market/depth'
    params = parse_params_to_str({'symbol':'btcusdt_spbl', 'limit': 20})
    body=''
    
    signStr = signature(timestamp, method, request_path+params, body, secret_key)
    print(signStr)
    
