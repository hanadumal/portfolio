from pprint import pprint
from util.request import Request
import json
import pandas as pd
import time


def parse_sse(result_sse):
    data = result_sse['result']
    # json {"data": null} 会被python解析为None
    if data is None:
        return None
    for col in data:
        avg_profit_rate   = col['AVG_PROFIT_RATE']    # 平均市盈率(倍）
        mkt_value         = col['MKT_VALUE']          # 总市价（亿元）
        negotiable_value  = col['NEGOTIABLE_VALUE']   # 流通总市价（亿元）
        tx_amount         = col['TX_AMOUNT']          # 成交金额（亿元）
        tx_num            = col['TX_NUM']             # 挂牌数
        total_mk_cap_rate = col['TOTAL_MK_CAP_RATE']  # 换手率
        cal_date          = col['CAL_DATE']           # 查询日期
        if col['PRODUCT_TYPE'] == '1':
            name = '主板A'
            return f"{name} {cal_date} 市盈率:{avg_profit_rate} 市值(亿):{mkt_value} 成交金额(亿):{tx_amount}"


def query_sse(dt_F):
    base_url='http://query.sse.com.cn/commonQuery.do?jsonCallBack=jsonpCallback125860&searchDate={date_F}&sqlId=COMMON_SSE_SJ_GPSJ_CJGK_DAYCJGK_C&stockType=90&_=1610390796012'
    url = base_url.format(date_F=dt_F)
    sse_resp = Request.request_url(url)
    if sse_resp is None:
        return None
    # print(sse_resp.text[20:-1])
    result = json.loads(sse_resp.text[20:-1])
    final_data = parse_sse(result)
    print(final_data)


if __name__ == '__main__':
    dts = pd.bdate_range(start='10/10/2020', end='12/31/2020')
    for i in dts:
        dt_str = i.strftime('%Y-%m-%d')
        # print(dt_str)
        # continue
        query_sse(dt_str)
        time.sleep(1)
        # print(type(i))
        # print(i.normalize())
        # print(i.fromisoformat())


