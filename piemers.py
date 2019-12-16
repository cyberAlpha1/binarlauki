# Pievienosim binarlaukus
import binarlauki as b

# uztaisam 1 + 2 * 3 augstu zalkti, ievietojam trīs rindu atstarpi un tad pievienjam 4 + 3 * 3 platuma ūsiņu, un iznākumu pārveidojam par C, C++, C#... bloka komentāru
iz = b.cfy(b.zalktis(3) + [''] * 3 + b.usins(3))
for i in iz:
	print(i)
