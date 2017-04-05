#!/bin/env/python
import sys

if len(sys.argv) != 2:
        sys.exit(1)

str = sys.argv[1]

frobbed = []
for i in str:
        frobbed.append(chr(ord(i)^42))

print "".join(frobbed)

//Or as a one-liner "".join(chr(ord(i)^42) for i in sys.argv[1])
