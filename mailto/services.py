#!/usr/bin/env python
# -*- coding: UTF-8 -*-

import urllib.request, urllib.parse, urllib.error

service = {}

def kerio(address, baseuri):
    print(address)
    return '%s/webmail/mailCompose.php?mailTo=%s' % (baseuri, urllib.parse.quote_plus(address))

service['kerio'] = {'func': kerio, 'args': ['address', 'baseuri']}
