#!/usr/bin/env python
# -*- encoding: utf-8 -*-
"""
@File    :   TencentDiscernImage.py
@Time    :   2019/8/26 21:35
@Author  :   Crisimple
@Github :    https://crisimple.github.io/
@Contact :   Crisimple@foxmail.com
@License :   (C)Copyright 2017-2019, Micro-Circle
@Desc    :   None
"""

from __future__ import print_function

import ssl, hmac, base64, hashlib
from datetime import datetime as pydatetime

try:
    from urllib import urlencode
    from urllib2 import Request, urlopen
except ImportError:
    from urllib.parse import urlencode
    from urllib.request import Request, urlopen

# 云市场分配的密钥Id
secretId = "AKIDOIGQ7v36FHuJD7D932G4Oz5Kr098l82w0Ge0"
# 云市场分配的密钥Key
secretKey = "D2jk9JqAB9je67q7S66u8w0R3oASNz8iYX2dOleC"
source = "market"

# 签名
datetime = pydatetime.utcnow().strftime('%a, %d %b %Y %H:%M:%S GMT')
signStr = "x-date: %s\nx-source: %s" % (datetime, source)
sign = base64.b64encode(hmac.new(secretKey.encode('utf-8'), signStr.encode('utf-8'), hashlib.sha1).digest())
auth = 'hmac id="%s", algorithm="hmac-sha1", headers="x-date x-source", signature="%s"' % (secretId, sign.decode('utf-8'))

# 请求方法
method = 'POST'
# 请求头
headers = {
    'X-Source': source,
    'X-Date': datetime,
    'Authorization': auth,
}
# 查询参数
queryParams = {
    'convert_to_jpg': '1',
    'img_base64': '',
    'needMorePrecise': '0',
    'typeId': '34'}
# body参数（POST方法下存在）
bodyParams = {
}
# url参数拼接
url = 'https://service-o8khspwt-1255468759.ap-beijing.apigateway.myqcloud.com/release/checkCode'
if len(queryParams.keys()) > 0:
    url = url + '?' + urlencode(queryParams)

request = Request(url, headers=headers)
request.get_method = lambda: method
if method in ('POST', 'PUT', 'PATCH'):
    request.data = urlencode(bodyParams).encode('utf-8')
    request.add_header('Content-Type', 'application/x-www-form-urlencoded')
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE
response = urlopen(request, context=ctx)
content = response.read()
if content:
    print(content.decode('utf-8'))
