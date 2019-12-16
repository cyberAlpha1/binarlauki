"""
------------#-----------------------#------------
----------#---#-----------------------#----------
--------#-------#-----------------------#--------
------#-----------#-----------------------#------
----#---------------#-----------------------#----
--#-------------------#-----------------------#--
#-----------------------#-----------------------#
--#-----------------------#-------------------#--
----#-----------------------#---------------#----
------#-----------------------#-----------#------
--------#-----------------------#-------#--------
----------#-----------------------#---#----------
------------#-----------------------#------------
"""


f = '#'
e = ' '

def pythonify(m):
	o = []
	o.append('"""')
	for i in m:
		o.append('' + i)
	o.append('"""')
	return o
def cfy(m):
	o = []
	o.append('/*')
	for i in m:
		o.append(' *  ' + i)
	o.append('*/')
	return o

def zalktis(s = 2):
	if s < 1:
		s = 1
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
