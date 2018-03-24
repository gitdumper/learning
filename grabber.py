#!/usr/bin/env python

import yaml
from pprint import pprint as pp
from netmiko import Netmiko

with open("../config/devices.yml") as f:
  devices = yaml.load(f)

for device in devices['devices']:
  dd = { 'host' : device['ip_addr'],
         'username' : device['username'],
         'password' : device['password'],
         'device_type' : 'cisco_ios'
       }

  nc = Netmiko(**dd)
  output = nc.send_command('show version')
  print('###!!! show version !!!###')
  print(output)
  print('\n\n')
  output = nc.send_command('show inventory')
  print('###!!! show inventory !!!###')
  print(output)

  

