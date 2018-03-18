# -*- coding:utf-8 -*-
from requests import get
from json import loads


def simsimi(info):
    url = "	http://sandbox.api.simsimi.com/request.p"
    with open("simsimi.key") as fp:
        key=fp.readline()
    json_payload = {"key": key,
                    "text": info,
                    "lc": "ch"
                    }
    res = get(url, json_payload)
    text = loads(res.content.decode("utf-8"))['response']
    return text


if __name__ == "__main__":
    print(simsimi("你叫什么"))
