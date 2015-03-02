import sys
if 0 > len(sys.argv) > 1:
        sys.exit(0)
str = sys.argv[1]
str = list(str)
xok = 0x2a
len = len(str)
kek = []
for x in xrange(0,len):
        kek.append(hex(ord(str[x])))
for x in xrange(0,len):
        kek[x] = hex(int(kek[x], 16) ^ int(hex(xok), 16))


def convert_hex_to_ascii(h):
    chars_in_reverse = []
    while h != 0x0:
        chars_in_reverse.append(chr(h & 0xFF))
        h = h >> 8

    chars_in_reverse.reverse()
    return ''.join(chars_in_reverse)
gee = ""
for x in xrange(0,len):
        gee = gee + convert_hex_to_ascii(int(kek[x], 16))

print gee
