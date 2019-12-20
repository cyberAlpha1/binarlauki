import binarlauki as b
import sys, getopt
import time

s = 3
l = 'cpp'

try:
    opts, args = getopt.getopt(sys.argv[1:], 'hf:e:f:s:l:', ['fill=', 'empty=', 'size=', 'lang='])
except getopt.GetoptError:
    print('oof')
    sys.exit(2)
for opt, arg in opts:
    if opt == '-h':
        print('ha ha, noobs')
        sys.exit()
    elif opt in ('-f', '--fill'):
         b.f = arg.replace('hash', '#').replace('space', ' ')
    elif opt in ('-e', '--empty'):
         b.e = arg.replace('space', ' ')
    elif opt in ('-s', '--size'):
         s = int(arg)
    elif opt in ('-l', '--lang'):
         l = arg

if l == 'py':
    izvade = b.py(b.zalktis(s) + [''] * 3 + b.usins(s))
elif l == 'cpp':
    izvade = b.cpp(b.zalktis(s) + [''] * 3 + b.usins(s))
else:
    izvade = b.zalktis(s) + [''] * 3 + b.usins(s) + [''] * 3 + b.jumis(s)
for rinda in izvade:
    print(rinda)
