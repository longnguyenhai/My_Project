from sys import argv
scrip,a,x,b = argv

if x == '+':
	cong = float(a) + float(b)
	print "Resul:", cong
elif x == '-':
	tru = float(a) - float(b)
	print "Resul: ", tru
elif x == '/':
	chia = float(a) / float(b)
	print "Resul:", chia
elif 	x == '*':
	nhan = float(a) * float (b)
	print "Resul:", nhan
	
else:
	print " Expression errors!"
	
 



