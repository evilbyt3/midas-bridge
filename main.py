from dotenv import load_dotenv
import os
import requests
# export REQUESTS_CA_BUNDLE="/home/vlaghe/proj/sec/burp_labs/burp.pem"
# export HTTP_PROXY="http://127.0.0.1:8080"
# export HTTPS_PROXY="http://127.0.0.1:8080"


class MidasAPI:
    def __init__(self, token):
        self.url = "https://api.midas.investments/ws.php"
        self.token = token
        self.initSesh()

    def initSesh(self):
        self.s = requests.Session()
        headers = {
            "Token": self.token,
            "Content-Type": "application/json",
            "Referer": "https://api.midas.investments/"
        }
        self.s.headers.update(headers)
    
    def getPortofolioStatus(self):
        try:
            data = {
                "operationName" : "stat",
                "variables": {},
                "query": "query stat {\n  stat {\n    id\n    weeklyIncomeEstimationUSD\n    totalBalanceUSD\n    __typename\n  }\n}\n"
            }
            r = self.s.post(self.url, json=data)
            if r.status_code == 200:
                return r.json()
            else:
                return -1

        except Exception as e:
            raise e


load_dotenv()
mapi = MidasAPI(os.getenv("TOKEN"))
print(mapi.getPortofolioStatus())




# data = {
#     "operationName" : "shareAssets",
#     "variables": {},
#     "query": "query shareAssets {\n  myFlatShares {\n    ...ShareAllFields\n    __typename\n  }\n  stat {\n    ...StatAllFields\n    __typename\n  }\n}\n\nfragment ShareAllFields on FlatShare {\n  id\n  assetId\n  value\n  valueFmt\n  depositAddress\n  depositAddressMessage\n  depositAddressMemo\n  hasTransaction\n  __typename\n}\n\nfragment StatAllFields on Stat {\n  id\n  weeklyIncomeEstimationUSD\n  totalBalanceUSD\n  __typename\n}\n"
# }
# 
# r = requests.post(URL, headers=headers, json=data)
# print(r.text)



