import http
import re
from urllib import parse

import requests

import settings
from utils import log

i: int = 0
with open("./headers.txt", "r") as tf:
    user_agents = tf.read().split('\n')


class MockText(object):
    def __init__(self, text, ua):
        self.text = text
        self.ua = ua


def reqDetail(cookies):
    global i
    if i == len(user_agents) - 1:
        i = 0
    else:
        i += 1
    headers = {
        "Cookie": cookies,
        "User-Agent": user_agents[i % 24],
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,"
                  "application/signed-exchange;v=b3;q=0.9",
        "Accept-Encoding": "gzip, deflate, br",
        "Accept-Language": "en-US,en;q=0.9",
        "Cache-Control": "no-cache",
        "Connection": "keep-alive",
        "DNT": "1",
        "Host": "hk.sz.gov.cn:8118",
        "Pragma": "no-cache",
        "Referer": settings.userCenterUrl,
        "Sec-Fetch-Dest": "document",
        "Sec-Fetch-Mode": "navigate",
        "Sec-Fetch-Site": "same-origin",
        "Sec-Fetch-User": "?1",
        "Upgrade-Insecure-Requests": "1",
    }
    res = requests.get(settings.detailUrl, headers=headers, verify=False, timeout=1)
    return res


def submit(submitParams):
    # n = json.dumps(submitParams)
    # m = MultipartEncoder(fields=submitParams)
    headers = {
        "Cookie": settings.cookie,
        "User-Agent": user_agents[i % 24],
        "Accept": "*/*",
        "Accept-Language": "en-US,en;q=0.9",
        "DNT": "1",
        "Host": "hk.sz.gov.cn:8118",
        "Referer": settings.confirmOrderUrl,
        "Content-Type": "application/x-www-form-urlencoded"
    }
    res = requests.post(settings.submitUrl, data=parse.urlencode(submitParams), headers=headers, verify=False)
    return res


def getDetail(cookies):
    while True:
        try:
            res = reqDetail(cookies)
        except:
            continue
        if res.status_code == http.HTTPStatus.OK and len(res.history) == 0:
            log("查询成功")
            return MockText(res.text, user_agents[i % 24])
        if res.status_code == http.HTTPStatus.FORBIDDEN:
            log("IP封禁")
            continue
        if len(res.history) != 0 and re.search('/error/index', res.history[0].headers['location']) is not None:
            log("未开放")
            continue
        else:
            log("未登录")
            continue


def getDetailMock():
    with open(settings.detailUrlMock, "r") as mock:
        return MockText(mock.read(), user_agents[i % 24])
