import mitmproxy.http
import redis

import settings
from mitmproxy import flowfilter

redis_conn = redis.Redis(host='127.0.0.1', port=6379, db=0)


class Interceptor:
    def __init__(self):
        # 添加网址过滤器
        self.filter = flowfilter.parse("~u " + settings.prehandleUrl)
        self.filter2 = flowfilter.parse("~u " + settings.verifyUrl)

    def request(self, flow: mitmproxy.http.HTTPFlow):
        # if flowfilter.match(self.filter, flow):
        #     ctx.log.info("match request")
        #     # 替换搜索词
        flow.request.query["entry_url"] = settings.confirmUrl.format(str(redis_conn.get('checkinDate'), 'utf-8'), str(redis_conn.get('t'), 'utf-8'),
                                                                     str(redis_conn.get('s'), 'utf-8'))
        print(flow.request.query)
        pass

    def response(self, flow: mitmproxy.http.HTTPFlow):
        if flowfilter.match(self.filter2, flow):
            # ctx.log.info("match response")
            # 添加/修改headers
            # flow.response.headers["md5"] = "00112233445566778899AABBCCDDEEFF"
            # flow.response.content = bytes("fuck you",encoding='utf8')
            # data = json.loads(flow.response.content)
            redis_conn.set('pass_ok_ticket', flow.response.content)


addons = [
    Interceptor()
]

"""
mitmweb  --listen-port 9999 --web-port 8848 --ignore-hosts ^hk\.sz\.gov\.cn$ -s mitmproxy.py
mitmdump  --listen-port 9999 --ignore-hosts ^hk\.sz\.gov\.cn$ -s mitmproxy.py
"""
