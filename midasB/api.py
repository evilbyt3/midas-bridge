import requests
import json
# export REQUESTS_CA_BUNDLE="/home/vlaghe/proj/sec/burp_labs/burp.pem"
# export HTTP_PROXY="http://127.0.0.1:8080"
# export HTTPS_PROXY="http://127.0.0.1:8080"

# Playground: https://api.midas.investments/
# Retrieve token by going to https://midas.investments/assets with burp activated


class MidasAPI:
    def __init__(self, token):
        self.url = "https://api.midas.investments/ws.php"
        self.token = token
        self.initSesh()


    # Helper function to make a POST request & return it's json
    def makeReq(self, data):
        try:
            r = self.s.post(self.url, json=data)
            if r.status_code == 200:
                return r.json()
            else:
                return -1
        except Exception as e:
            raise e

    # Initialize the session to the API
    def initSesh(self):
        self.s = requests.Session()
        headers = {
            "Token": self.token,
            "Content-Type": "application/json",
            "Referer": "https://api.midas.investments/"
        }
        self.s.headers.update(headers)
    

    # Get overall status 
    # Returns: {'id': '31129', 'weeklyIncomeEstimationUSD': 11.542319033243432, 'totalBalanceUSD': 3100.527715633625, '__typename': 'Stat'}
    def getPortofolioStatus(self):
        data = {
            "operationName" : "stat",
            "variables": {},
            "query": "query stat {\n  stat {\n    id\n    weeklyIncomeEstimationUSD\n    totalBalanceUSD\n    __typename\n  }\n}\n"
        }
        return self.makeReq(data)['data']['stat']


    # Retrieve all the assets in your portofolio 
    # Returns a list of active assets: 
    # [
    #     {
    #         "assetId": "35",
    #         "valueFmt": "0.477383915058738033",
    #         "coinTitle": "Ethereum",
    #         "coinSymbol": "ETH",
    #         "coinUsd": 4346.31,
    #         "depositAddress": "0x430fbe103ad98eafec83bc45bcb0849935ec984f",
    #         "hasTransaction": true,
    #         "__typename": "FlatShare"
    #     },
    #     {...}
    # ]
    def getAllAssets(self):
        data = {
            "operationName" : "shareAssets",
            "variables": {},
            "query": "query shareAssets {\n  myFlatShares {\n    ...ShareAllFields\n    __typename\n  }\n}\n\nfragment ShareAllFields on FlatShare {\n  assetId\n  valueFmt\n  coinTitle\n  coinSymbol\n  coinUsd\n  depositAddress\n  hasTransaction\n  __typename\n}"
        }

        return self.makeReq(data)['data']['myFlatShares']


    # Gets info about a specific asset 
    #   @assetId -- the asset id
    #
    # Returns a json like: {'title': 'Midas', 'apy': 0.09551780895428985, 'priceUSD': 27.7, 'symbol': 'MIDAS_COIN', 'kind': 'MN'}
    def getAsset(self, assetId):
        data = {
            "operationName" : "asset",
            "variables": {},
            "query": f"query asset {{\n  assetById(id: {assetId}) {{\n    title,\n    apy,\n    priceUSD,\n    symbol,\n    kind\n  }}\n}}\n"
        }
        res = self.makeReq(data)['data']['assetById']
        return res





# if __name__ == "__main__":
#     load_dotenv()
#     mapi = MidasAPI(os.getenv("TOKEN"))
#     print(mapi.getPortofolioStatus())
#     print(json.dumps(mapi.getAllAssets(), indent=4))
#     print(mapi.getAsset(2))
