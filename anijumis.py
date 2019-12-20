import binarlauki as b
import time

es = [' ']
fs = ['#', '$', '%', '&', '£', '™', '±']

for i in range(0, 25):
    for ef in fs:
        b.f = ef
        for ee in es:
            b.e = ee
            time.sleep(0.1)
            izvade = (b.jumis(2) + [''] * 3 + b.jumis(3) + [''] * 3 + b.jumis(4))
            print('\n\n\n\n\n')
            for rinda in izvade:
	            print(rinda)
