from enum import Enum
import logging

class FirstResult(Enum):
    INCREASE_DOWN_HOR = 1
    INCREASE_UP_HOR = 2
    DECREASE_UP_HOR = 3
    DECREASE_DOWN_HOR = 4

class Action(Enum):
    BUY = 1
    SELL = 2


class ThreeFilter(object):
    def __init__(self):
        pass

    def first_filter(self, macd):
        """
        判断MACD柱，最近两根的变化趋势。如果相邻斜率为正
        :param macd: dict
        :return:
        """
        vs = list(macd.values())
        change = vs[-1] - vs[-2]
        if change > 0 and vs[-1] < 0:
            # 斜率为正，最近的MACD柱在0线下
            result = FirstResult.INCREASE_DOWN_HOR
        elif change > 0 and vs[-1] > 0:
            # 斜率为正，最近的MACD柱在0线上
            result = FirstResult.INCREASE_UP_HOR
        elif change < 0 and vs[-1] > 0:
            # 斜率为负，最近MACD在0线上
            result = FirstResult.DECREASE_UP_HOR
        elif change < 0 and vs[-1] < 0:
            # 斜率为负，最近MACD柱在0线下
            result = FirstResult.DECREASE_DOWN_HOR
        logging.info(f"第一层过滤结果：{result}")
        return result

    def second_filter(self, close_prices, newest_vol):
        """ 计算窗口为2的，强力指标EMA
        :param close_prices: [(time, price), (time, price)]
        :param newest_vol: tuple (time, price)
        :return:
        """
        price_diff = (close_prices[-1][1] - close_prices[-2][1])
        logging.info(f"第二层过滤：价格差{price_diff} 最新成交量{newest_vol}")
        strong_index = price_diff * newest_vol
        return strong_index

    def third_filter(self, close_prices, ema1s, size=14):
        """ 第三层控制买入信号
        # Todo: 是否换成更短的时间周期，1小时的时间窗口
        :param close_prices: 收盘价，[(时间，收盘价)]
        :param ema1s: 短期的EMA      {时间：收盘价, 时间：收盘价}
        :return: 在最近的size窗口内，收盘价跌破快速EMA的均价
        """
#         print(ema1s)
#         print(close_prices)
        
        fall_over_count = 0
        fall_over_totoal = 0
        for i in range(1, size+1):
            diff = close_prices[-i][1] - list(ema1s.values())[-i]
            if diff < 0:
                fall_over_count += 1
                # 这个值为负数，不取abs, 下面直接跟最新价格相加
                fall_over_totoal += diff
        newest_price = close_prices[-1][1]
        delta = 0
        # 计算平均收盘价跌破快速EMA的均值
        if fall_over_count != 0:
            delta = fall_over_totoal/fall_over_count
        else:
            delta = 0
        logging.info(f"第三层过滤: 最新价格 {newest_price} 平均跌破:{delta}")
        return newest_price + delta


    def run(self, long_macd, medium_close, medium_ema1, medium_newest_vol):
        """ Todo: 现在只能给出买入信号
        :param long_macd: dict
        :param medium_close:
        :param medium_ema1:
        :param medium_newest_vol:
        :return:
        """
        first_flag = self.first_filter(long_macd)
        second_flag = self.second_filter(medium_close, medium_newest_vol)
        if first_flag in (FirstResult.INCREASE_UP_HOR, FirstResult.INCREASE_DOWN_HOR):
            if second_flag < 0:
                action = Action.BUY
                buy_price = self.third_filter(medium_close, medium_ema1)
                return action, buy_price
        elif first_flag in (FirstResult.DECREASE_UP_HOR, FirstResult.DECREASE_DOWN_HOR):
            action = Action.SELL
            sell_price = None
            return action, sell_price
        else:
            print(f"第一层动作结果未知")
        return None, None
