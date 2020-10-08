#!/usr/bin/python3

print("content-type: text/html")
print()

import subprocess as sp
import cgi
form = cgi.FieldStorage()

osname=form.getvalue("x")

cmd = "sudo docker rm {}".format(osname)

output = sp.getstatusoutput(cmd)

status = output[0]
out = output[1]


if status == 0:
    print("os successfully removed  named {}  ..".format(osname))
else:
    print("some error ... {} ".format(out))
