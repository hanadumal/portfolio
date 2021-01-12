"""
Encapsul of requests
"""
import logging
from urllib import parse

import requests


class Request(object):
    logger = logging.getLogger(f'{__name__}.Request')

    @staticmethod
    def request_url(url, params=None, user_agent='Mozilla 5.10'):
        """If return status not 200, return None, else return a dict.
        :param url:
        :param params:
        :param user_agent:
        :return:
        """
        headers = {
            # "Accept-Charset": "UTF-8",
            # "Content-type": "application/json",
            "Referer": 'http://www.sse.com.cn/'
        }
        post_data = parse.urlencode(params) if params is not None else ''
        raw_data = requests.get(url, headers=headers)
        if raw_data.status_code == 200:
            return raw_data
            result_data = raw_data.json()
            Request.logger.info(result_data)
            return result_data
        return None