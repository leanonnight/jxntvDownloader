import traceback

from bs4 import UnicodeDammit
from bs4 import BeautifulSoup

import requests
import time
import logging


import Util.CommonUtil as util

class RequestUtil:

    headers = {

        'Accept': "*/*",
        'accept-encoding': "gzip, deflate",
        'accept-language': "zh-CN,zh;q=0.9",
        'connection': "keep-alive",
        'Host': "app.yun.jxntv.cn",
        'Referer': "http://v.jxntv.cn/",
        'user-agent': "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.90 Safari/537.36",
    }

    def get_html(self, url, header=headers):
        startTime = time.time()
        try:
            r = requests.get(url, timeout=10, headers=header)
            r.raise_for_status()
            # 自动选择合适的编码方式
            # dammit = UnicodeDammit(r.content, ["utf-8", "gbk"])
            # html = dammit.unicode_markup
            r.encoding = "utf-8"
            html = r.text
            endTime = time.time()
            print("获取url:" + url + "成功, 用时:" + util.time_to_str(startTime - endTime))
            return html
        except Exception:
            endTime = time.time()
            traceback.print_exc()
            print("获取url:" + url + "错误, 用时:" + util.time_to_str(startTime - endTime))
            return None

if __name__ == '__main__':
    html = RequestUtil().get_html("http://pc.yun.jxntv.cn/p/412204.html")
    print(html)
    # soup = BeautifulSoup(html, "lxml")


    # print(soup.prettify())
    #
    # news_items = soup.find_all("div", attrs={"class": 'news-item'})
    #
    # for news_item in news_items:
    #     print(news_item)