#!/usr/bin/env python

import yaml
from pprint import pprint as pp
from snmp_helper import snmp_get_oid, snmp_extract

with open("../store/inventory/devices.yml") as f:
  devices = yaml.load(f)

for device in devices['devices']:
  a_device = (device['ip_addr'], device['snmp_ro'], 161)
  OID = '1.3.6.1.2.1.1.5.0' #hostname

  snmp_data = snmp_get_oid(a_device, oid=OID)
  output = snmp_extract(snmp_data)
  print(output)
  

