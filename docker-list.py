#!/usr/bin/python3

print("content-type: text/html")
print()

import subprocess as sp
import cgi
form = cgi.FieldStorage()

cmd = "sudo docker ps"

output = sp.getstatusoutput(cmd)

status = output[0]
out = output[1]


if status == 0:
    print("List of Running docker container:- {}".format(out))
else:
    print("some error ... {} ".format(out))
