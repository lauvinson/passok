import time
from urllib import parse
from urllib.parse import urlparse

from selectolax.parser import HTMLParser

import req


# redis_conn = redis.Redis(host='127.0.0.1', port=6379, db=0)


def get_time_stamp():
    ct = time.time()
    local_time = time.localtime(ct)
    data_head = time.strftime("%Y-%m-%d %H:%M:%S", local_time)
    data_secs = (ct - int(ct)) * 1000
    time_stamp = "%s:%03d" % (data_head, data_secs)
    return time_stamp


def log(data):
    print(get_time_stamp(), ' ', data, ' ', req.user_agents[req.i])


def getDetailParams(container, text):
    """
    从detail源码中获取所需参数
    :param container: 参数容器
    :param text: detail网页源码
    :param index: 获取下表
    :return:
    """
    tree = HTMLParser(text)
    nodes = tree.css('a.orange')
    if len(nodes) == 0:
        return
    node = nodes[-1]
    query = parse.parse_qs(urlparse(node.attributes.get('href')).query)
    container['checkinDate'] = query['checkinDate'][0]
    container['s'] = query['s'][0]
    container['t'] = str(query['t'][0])
    # redis_conn.set('checkinDate', container['checkinDate'])
    # redis_conn.set('s', container['s'])
    # redis_conn.set('t', container['t'])
