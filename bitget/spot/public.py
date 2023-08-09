import sys; sys.path.append('..')
from client import Client
from consts import *

# class Public(Client):
#     def __init__(public_api_key, secret_api_key, passphrase, use_server_time=False, first=False):
#         super().__init__(public_api_key, secret_api_key, passphrase, use_server_time, first)

#     def get_server_time(self):
#         return self._request_without_params(GET, SERVER_TIMESTAMP_URL)
    
# if __name__ == '__main__':
#     api_key = "bg_ee3e1442a70b7d17d772b8082ae9d990"
#     secret_key = "0479dab05c985b4ce3e02e0b052baadbb9711d6e20035a73c278c19b5baec966"
#     passphrase = "A99093003626a"  # Password

#     p = Public(api_key, secret_key, passphrase, True, True)
#     print(p.get_server_time())
