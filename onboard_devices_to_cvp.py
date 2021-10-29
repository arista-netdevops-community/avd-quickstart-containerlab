#!/usr/bin/env python3

import json
import sys
import requests
import requests.packages.urllib3 as urllib3
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

cvp_url_prefix = 'https://192.168.122.241:443'
cvp_username = 'cvpadmin'
cvp_password = 'arista123'
devices_to_onboard = [
    # spines
    '192.168.123.11', '192.168.123.12',
    # leafs
    '192.168.123.21', '192.168.123.22', '192.168.123.23', '192.168.123.24'
]

class CVP:

    def __init__(self, url_prefix, cvp_username, cvp_password):
        self.session = requests.session()
        self.session.verify = False
        self.cvp_url_prefix = url_prefix
        self.timeout = 180
        # authenticate
        url = self.cvp_url_prefix + '/web/login/authenticate.do'
        authdata = {'userId': cvp_username, 'password': cvp_password}
        resp = self.session.post(url, data=json.dumps(authdata), timeout=self.timeout)
        if resp.raise_for_status():
            sys.exit('ERROR: Received wrong status code when connecting to CVP!')

    def onboard(self):
        url = self.cvp_url_prefix + '/cvpservice/inventory/devices'
        d = json.dumps({
            'hosts': devices_to_onboard
        })
        resp = self.session.post(url, data=d, timeout=self.timeout)
        if resp.raise_for_status():
            sys.exit('ERROR: Received wrong status code when connecting to CVP!')

if __name__ == "__main__":
    cv = CVP(cvp_url_prefix, cvp_username, cvp_password)
    cv.onboard()
