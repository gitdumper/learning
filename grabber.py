#!/usr/bin/env python

import yaml
from pprint import pprint as pp
from netmiko import Netmiko

with open("../store/inventory/devices.yml") as f:
  devices = yaml.load(f)

for device in devices['devices']:
  dd = { 'host' : device['ip_addr'],
         'username' : device['username'],
         'password' : device['password'],
         'device_type' : 'cisco_ios'
       }

  nc = Netmiko(**dd)
  nf = open('../store/output/{}.out'.format(device['host']), 'w')
  output = nc.send_command('show version')
  nf.write('###!!! show version !!!###\n')
  nf.write(output)
  nf.write('\n')
  output = nc.send_command('show inventory')
  nf.write('###!!! show inventory !!!###\n')
  nf.write(output)
  nf.write('\n')
  nf.close()
  nc.disconnect()
  

