import requests
from pprint import pprint
# Basic factor
point_limit = -100
# MACD's factor
ma1_size = 7
ma2_size = 30
dea_size = 9


# Monitor Coin factor
k15_symbols ={'IOTA/USDT', 'BTC/USDT',  'ETH/USDT', 'XRP/USDT', 'EOS/USDT',
              'LTC/USDT',  'BCH/USDT',  'ETC/USDT', 'XLM/USDT', 'ADA/USDT',
              'XMR/USDT',  'DASH/USDT', 'ZEC/USDT', 'OMG/USDT', 'BSV/USDT'}

main_symbols={'BTC/USDT', 'ETH/USDT', 'BNB/USDT'}
all_symbols =set.union(k15_symbols, main_symbols)
dev_symbols={'BTC/USDT'}
# all_symbols={'BTC/USDT', 'ETH/USDT', 'BNB/USDT'}
# all_symbols={'SAND/USDT', 'BTC/USDT'}
# all_symbols={'BTC/USDT'}
all_symbols = {'SAND/USDT', 'NULS/USDT', 'TOMO/USDT', 'AAVE/USDT'}


def request_url(url, params=None, user_agent='Mozilla 5.10'):
    """If return status not 200, return None, else return a dict.
    :param url:
    :param params:
    :param user_agent:
    :return:
    """
    raw_data = requests.get(url)
    if raw_data.status_code == 200:
        result_data = raw_data.json()
        return result_data
    return None

cmc_url = "https://api.coinmarketcap.com/data-api/v3/cryptocurrency/listing?start=1&limit=100&sortBy=market_cap&sortType=desc&convert=USD,btc,eth&cryptoType=all&tagType=all&aux=ath,atl,high24h,low24h,num_market_pairs,cmc_rank,date_added,tags,platform,max_supply,circulating_supply,total_supply,volume_7d,volume_30d"
cmc_coin_list = request_url(cmc_url)['data']['cryptoCurrencyList']
cmc_coin_top100 = [info['symbol']+'/USDT' for info in cmc_coin_list if 'USD' in [quote['name'] for quote in info['quotes']]]
# pprint(cmc_coin_list[:10])
# pprint(cmc_coin_top100)