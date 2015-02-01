#!/usr/bin/env python
# -*- coding: utf-8 -*-

import escape
import json
import httplib2
import traceback

class BaiduTranslate(object):
    def __init__(self, client_id):
        self.client_id = client_id
        self.http = httplib2.Http()
        self.api = "http://openapi.baidu.com/public/2.0/bmt/translate"

    def translate(self, q, fr="auto", to="auto"):
        q = escape.xhtml_unescape(q)
        q = escape.url_escape(q)
        _body = "client_id=%s&q=%s&from=%s&to=%s" % (self.client_id, q, fr, to)
        _max_retry = 3
        _tried = 0
        _response = _content = None
        while _tried < _max_retry:
            try:
                _response, _content = self.http.request(self.api, "POST", _body)
                _tried = 3
            except:
                print traceback.format_exc()
                pass
            _tried += 1

        try:
            _result = json.loads(_content)
            return "\n".join(p['dst'] for p in _result['trans_result'])
        except:
            print traceback.format_exc()
            pass
        return None

if __name__ == "__main__":
    import sys
    t = BaiduTranslate(sys.argv[1])
    print t.translate(sys.argv[2])

