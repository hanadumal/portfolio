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
