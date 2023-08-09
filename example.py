from bitget.client import *

api_key = "bg_ee3e1442a70b7d17d772b8082ae9d990"
secret_key = "0479dab05c985b4ce3e02e0b052baadbb9711d6e20035a73c278c19b5baec966"
passphrase = "A99093003626a"  # Password

cli = Client(api_key, secret_key, passphrase, True)
a = cli._request_with_params(c.GET, "/api/spot/v1/notice/queryAllNotices", {"languageType":"en_US"})['data']

print(a[-1])




