import redis
import requests

import req
from utils import log

requests.packages.urllib3.disable_warnings()

redis_conn = redis.Redis(host='127.0.0.1', port=6379, db=0)

# 构造请求参数
submitParams = {
    'checkinDate': '2022-06-12',
    'houseType': '1'
}


def ticket():
    log("验证通过")


def expose(w):
    w.expose(ticket)  # expose a function during the runtime
    w.evaluate_js('pywebview.api.ticket()')


def validate(ua):
    pass
    # entry_url = settings.confirmUrl.format(submitParams['checkinDate'], submitParams['t'], submitParams['s'])
    # validatePreHandleUrl = 'https://t.captcha.qq.com/cap_union_prehandle?aid=2060591863' \
    #                        '&protocol=https' \
    #                        '&accver=1' \
    #                        '&showtype=popup' \
    #                        '&ua=TW96aWxsYS81LjAgKE1hY2ludG9zaDsgSW50ZWwgTWFjIE9TIFggMTBfMTVfNykgQXBwbGVXZWJLaXQvNTM3LjM2IChLSFRNTCwgbGlrZSBHZWNrbykgQ2hyb21lLzEwMi4wLjAuMCBTYWZhcmkvNTM3LjM2' \
    #                                      '&noheader=1' \
    #                                      '&fb=1' \
    #                                      '&aged=0' \
    #                                      '&enableAged=0' \
    #                                      '&enableDarkMode=0' \
    #                                      '&grayscale=1' \
    #                                      '&clientype=2' \
    #                                      '&cap_cd=' \
    #                                      '&uid=' \
    #                                      '&wxLang=' \
    #                                      '&lang=en-US' \
    #                                      '&entry_url=' + entry_url + '' \
    #                                                                  '&elder_captcha=0' \
    #                                                                  '&js=%2Ftcaptcha-frame.346c1088.js' \
    #                                                                  '&login_appid=' \
    #                                                                  '&wb=1' \
    #                                                                  '&subsid=1' \
    #                                                                  '&callback=_aq_752436' \
    #                                                                  '&sess= '
    # pre_res = requests.get(validatePreHandleUrl, verify=False)
    # pre_res_json = json.loads(pre_res.text[re.search('{', pre_res.text).start(): -1])
    # sess = pre_res_json['sess']
    # sid = pre_res_json['sid']
    # validateShowHandleUrl = 'https://t.captcha.qq.com/cap_union_new_show?' \
    #                         'aid=' + str(settings.appId) + \
    #                         '&protocol=https' \
    #                         '&accver=1' \
    #                         '&showtype=popup' \
    #                         '&ua=TW96aWxsYS81LjAgKE1hY2ludG9zaDsgSW50ZWwgTWFjIE9TIFggMTBfMTVfNykgQXBwbGVXZWJLaXQvNTM3LjM2IChLSFRNTCwgbGlrZSBHZWNrbykgQ2hyb21lLzEwMi4wLjAuMCBTYWZhcmkvNTM3LjM2' \
    #                         '&noheader=1' \
    #                         '&fb=1' \
    #                         '&aged=0' \
    #                         '&enableAged=0' \
    #                         '&enableDarkMode=0' \
    #                         '&grayscale=1' \
    #                         '&clientype=1' \
    #                         '&sess=' + sess + \
    #                         '&fwidth=0' \
    #                         '&sid=' + sid + \
    #                         '&wxLang=' \
    #                         '&tcScale=1' \
    #                         '&uid=' \
    #                         '&cap_cd=' \
    #                         '&rnd=341334' \
    #                         '&prehandleLoadTime=40' \
    #                         '&createIframeStart=' + str(int(round(time.time() * 1000))) + \
    #                         '&global=0' \
    #                         '&subsid=2'
    redis_conn.set('validateShowHandleUrl', 'validateShowHandleUrl')


def run():
    res = req.getDetail()
    print(res.text)
    # getDetailParams(submitParams, res.text)
    # validate(res.ua)
    # log("等待验证")
    # while True:
    #     t = redis_conn.get("pass_ok_ticket")
    #     if t is not None:
    #         tick_json = json.loads(str(t, 'utf-8'))
    #         ticket = tick_json['ticket']
    #         ranstr = tick_json['randstr']
    #         submitParams['ticket'] = ticket
    #         submitParams['randStr'] = ranstr
    #         log(submitParams)
    #         while True:
    #             try:
    #                 submitRes = req.submit(submitParams)
    #             except:
    #                 continue
    #             log("提交结果")
    #             log(submitRes.text)
    #             log("=============")
    #             if submitRes.status_code != http.HTTPStatus.OK:
    #                 continue
    #             break
    #         redis_conn.delete("pass_ok_ticket")
    #         break
    # log("程序执行结束.....")


if __name__ == '__main__':
    run()
    # options = webdriver.Options()
    # 设置代理
    # options.add_argument("--proxy-server=http://127.0.0.1:9999")
    # specify headless mode
    # options.add_argument('headless')
    # specify the desired user agent
    # options.add_argument(f'user-agent={req.user_agents[req.i % 24]}')
    # 一定要注意，=两边不能有空格，不能是这样--proxy-server = http://202.20.16.82:10152
    # browser = webdriver.WebDriver(options=options)
    # threading.Thread(target=lambda: run()).start()
    # while True:
    #     vUrl: Awaitable = redis_conn.get("validateShowHandleUrl")
    #     if vUrl is not None:
    #         redis_conn.delete("validateShowHandleUrl")
    #         app = QApplication(sys.argv)
            # proxy = QtNetwork.QNetworkProxy()
            # proxy.setType(QtNetwork.QNetworkProxy.HttpProxy)
            # proxy.setHostName("127.0.0.1")
            # proxy.setPort(9999)
            # QtNetwork.QNetworkProxy.setApplicationProxy(proxy)
            # log(vUrl)
            # window = MainWindow(str(vUrl, 'utf-8'))
            # window.show()
            # sys.exit(app.exec_())
    # window = webview.create_window('请快速验证', html='<h1>请快速验证通过!<h1>', width=390, height=844)
    # webview.start(run, window, debug=True)
