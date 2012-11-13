#!/usr/bin/env python
# -*- coding: UTF-8 -*-

"""MailTo"""

__name__ = "mailto"
__author__ = 'Shane R. Spencer'
__email__ = "shane@bogomip.com"
__license__ = 'MIT'
__copyright__ = '2012 Shane R. Spencer'
__version__ = '0.0.1'
__status__ = "Prototype"

import re
import cgi

from bottle import route, request, run, redirect

from mailto import services

pattern = re.compile("^mailto:", re.IGNORECASE)

def getaddress(s):
    """ Simply remove mailto and do a basic email formatting check """
    s = pattern.sub('', s)
    return s

@route('/mailto')
def index():
    service = services.service.get(request.query.get('service'))
    
    address = ''
    if 'mailto' in request.query:
        address = getaddress(request.query.mailto)
    else:
        for k, v in request.query.iteritems():
            if '@' in k:
                address = getaddress(k)

    kwargs = {}
    for arg in service['args']:
        var = vars().get(arg, request.query.get(arg, None))
        if var:
            kwargs[arg] = var
            
    print service['args'], kwargs.keys()
    if set(service['args']) == set(kwargs.keys()):
        newurl = service['func'](**kwargs)
        redirect(newurl)

    return "FAIL"

def run_server():
    run(host='0.0.0.0', port=8080, reloader=True, debug=True, interval=0)
    
if __name__ == '__main__':
    run_server()
