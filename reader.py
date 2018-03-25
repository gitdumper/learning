#!/usr/bin/env python

from pprint import pprint as pp
import re

with open("../store/output/pynet-rtr1.out") as f:
  output = f.read()

z = re.findall(r'###!!! (.+) !!!###', output)
y = re.split(r"###!!! .+ !!!###",output, flags=re.M)

x = dict()
x[z[0]] = y[1].lstrip('\n')
x[z[1]] = y[2].lstrip('\n')
print(x)
