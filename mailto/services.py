#!/usr/bin/env python
# -*- coding: UTF-8 -*-

import urllib

service = {}

def kerio(address, baseuri):
    print address
    return '{baseuri}/webmail/mailCompose.php?mailTo={address}'.format(baseuri=baseuri, address=urllib.quote_plus(address))

service['kerio'] = {'func': kerio, 'args': ['address', 'baseuri']}
