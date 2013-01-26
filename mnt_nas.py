#! /usr/bin/env python

import pexpect
import sys
import base64
import config

password = base64.b64decode(config.SUDO_PASSWORD)
cmd = '''sudo mount_afp -o group=codein,user=codein  afp://codein:rvarghe1@GoFlexHome.local/codein/GoFlex%20Home%20Public /media/goflex_home/'''
print cmd

p = pexpect.spawn(cmd)

i = p.expect([".* password .*", pexpect.EOF])
p.sendline(password)