"""
----#-------#----
--#---#---#---#--
#-------#-------#
------#---#------
----#-------#----
--#-----------#--


------#-----------#------
----#---#-------#---#----
--#-------#---#-------#--
#-----------#-----------#
----------#---#----------
--------#-------#--------
------#-----------#------
----#---------------#----
--#-------------------#--


--------#---------------#--------
------#---#-----------#---#------
----#-------#-------#-------#----
--#-----------#---#-----------#--
#---------------#---------------#
--------------#---#--------------
------------#-------#------------
----------#-----------#----------
--------#---------------#--------
------#-------------------#------
----#-----------------------#----
--#---------------------------#--
"""

f = '#'
e = ' '

def py(m):
	o = []
	o.append('"""')
	for i in m:
		o.append('' + i)
	o.append('"""')
	return o
def cpp(m):
	o = []
	o.append('/*')
	for i in m:
		o.append(' *  ' + i)
	o.append('*/')
	return o

def zalktis(s = 2):
	o = []
	last = s * 2
	for i in range(0, 1 + last):
		sk = abs((1 + s) - i - 1)
		o.append(e * (sk * 2) + f + e * ((s + 1 - sk - 1) * 2))
	for i in range(1, 1 + (s * 2)):
		sk = (i * 2 - 1)
		o[i] += e * sk + f
	for i in range(0, last):
		sk = (i * 2 - 1)
		o[i] += e * (last * 2 - sk - 2)
	for i in range(0, last):
		sk = abs((1 + s) - i - 1)
		o[i] += (e * ((s * 2) - sk * 2) + f)
	for i in range(0, last + 1):
		sk = abs((1 + s) - i - 1)
		o[i] += e * (sk * 2)
	return o

def usins(s = 2):
	o = []
	last = s * 2
	topBot = (f + e) * (s + 2) + e * (s * 2) + (f + e) * (s + 1) + f
	vert = e * (s * 2 + 2) + f + e * (1 + s * 2) + f + e * (s * 2 + 2)
	line = (f + e) * (3 + s * 3) + f
	o.append(topBot)
	for i in range(0, s):
		o.append(vert)
	o.append(line)
	for i in range(0, s):
		o.append(vert)
	o.append(line)
	for i in range(0, s):
		o.append(vert)
	o.append(topBot)
	return o

def jumis(s = 2):
	o = []
	for i in range(0, 0 + s * 3):
		o.append([e] * (17 + (8 * (s - 2))))
	for i in range(0, len(o)):
		o[len(o) - i - 1][2 + i * 2] = f
		o[len(o)-i-1][(17 + (8 * (s - 2)))-3-(i*2)] = f
	for i in range(0, s + 1):
		o[s + 1 - i - 1][2 + i * 2-2] = f
		o[s + 1 - i - 1][(17 + (8 * (s - 2))) - (i * 2) - 1] = f
	o2 = []

	for i in o:
		o2.append('')
		for c in i:
			o2[len(o2) - 1] += c
	return o2
