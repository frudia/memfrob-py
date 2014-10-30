"""YOUR STRING GOES IN AS STR -- FOR NOW YOU HAVE TO PUT COMMAS AFTER EVERY CHARACTER, I'LL FIX THIS IN THE NEXT RELEASE."""
str = "C,G,C,D,S,E,_,X,G,K,I,B,C,D,O,Y,^,O,K,F,C,D,M,S,E,_,X,L,F,K,M,Y"
str = str.split(',')
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
