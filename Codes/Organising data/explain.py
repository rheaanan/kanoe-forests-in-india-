import csv
import re
f2 = open('fvsr.csv')
csv_f2 = csv.reader(f2)
l2007 = []
l2008 = []
l2009 = []
l2010 = []
l2011 = []
l2012 = []
l2013 = []
for line in csv_f2:
	#print line
	if(line[1] == '2007'):
		l2007.append(line)
	elif(line[1] == '2008'):
		l2008.append(line)
	elif(line[1] == '2009'):
		l2009.append(line)
	elif(line[1] == '2010'):
		l2010.append(line)
	elif(line[1] == '2011'):
		l2011.append(line)
	elif(line[1] == '2012'):
		l2012.append(line)
	elif(line[1] == '2013'):
		l2013.append(line)
dip78f = 0
dip78r = 0
dip89f = 0
dip89r = 0
dip910f = 0
dip910r = 0
dip1011f = 0
dip1011r = 0
dip1112f = 0
dip1112r = 0
dip1213f = 0
dip1213r = 0
#print l2007[1][0],l2008[1][0]
for i in range(len(l2007)):
	if(l2007[i][0] == l2008[i][0] == l2009[i][0] == l2010[i][0]  == l2011[i][0] == l2012[i][0] == l2013[i][0]):
		df78 = ((float(l2008[i][2]) - float(l2007[i][2]))/ float(l2007[i][2]))*100
		dr78 = ((float(l2008[i][3]) - float(l2007[i][3]))/float(l2007[i][3]))*100
		df89 = ((float(l2009[i][2]) - float(l2008[i][2]))/ float(l2008[i][2]))*100
		dr89 = ((float(l2009[i][3]) - float(l2008[i][3]))/float(l2008[i][3]))*100
		df910 = ((float(l2010[i][2]) - float(l2009[i][2]))/ float(l2009[i][2]))*100
		dr910 = ((float(l2010[i][3]) - float(l2009[i][3]))/float(l2009[i][3]))*100
		df1011 = ((float(l2011[i][2]) - float(l2010[i][2]))/ float(l2010[i][2]))*100
		dr1011 = ((float(l2011[i][3]) - float(l2010[i][3]))/float(l2010[i][3]))*100
		df1112 = ((float(l2012[i][2]) - float(l2011[i][2]))/ float(l2011[i][2]))*100
		dr1112 = ((float(l2012[i][3]) - float(l2011[i][3]))/float(l2011[i][3]))*100
		df1213 = ((float(l2013[i][2]) - float(l2012[i][2]))/ float(l2012[i][2]))*100
		dr1213 = ((float(l2013[i][3]) - float(l2012[i][3]))/float(l2012[i][3]))*100
		print l2007[i][0] 
		dip78f += df78
		dip78r += dr78
		dip89f += df89
		dip89r += dr89
		dip910f += df910
		dip910r += dr910
		dip1011f += df1011
		dip1011r += dr1011
		dip1112f += df1112
		dip1112r += dr1112
		dip1213f += df1213
		dip1213r += dr1213
		

dip78f = dip78f/len(l2007)
dip78r = dip78r/len(l2007)
dip89f = dip89f/len(l2007)
dip89r = dip89r/len(l2007)
dip910f = dip910f/len(l2007)
dip910r = dip910r/len(l2007)
dip1011f = dip1011f/len(l2007)
dip1011r = dip1011r/len(l2007)
dip1112f = dip1112f/len(l2007)
dip1112r = dip1112r/len(l2007)
dip1213f = dip1213f/len(l2007)
dip1213r = dip1213r/len(l2007)

print "2007/2008",dip78f,dip78r
print "2008/2009",dip89f,dip89r
print "2009/2010",dip910f,dip910r
print "2010/2011",dip1011f,dip1011r
print "2011/2012",dip1112f,dip1112r
print "2012/2013",dip1213f,dip1213r


	
	