'''import csv 
import os

nf = open("Forest2013.csv",'w')
csv_w = csv.writer(nf,delimiter = ",")

files =  os.walk("Forest 2013")
for fi in files:
	fi2 = list(fi)[2]

data = []
l = []
for fi in fi2:
	f2 = open('Forest 2013/'+fi)
	csv_f2 = csv.reader(f2)
	for i in csv_f2:
		l.append(i)
	data.append(l)
	l = []
#print data

for i in data:
	for j in i[1: ][ :-1]:
		csv_w.writerow(j)'''


import xlrd
import os
import xlwt
fi2 = []
files =  os.walk("Forest 2011")
for fi in files:
	fi2 = list(fi)[2]

book = xlwt.Workbook(encoding="utf-8")
sheet1 = book.add_sheet("Sheet 1",cell_overwrite_ok=True)

data = []
temp = []
b = 0
e = 0
cnt = 0
for fi in fi2:
	f_l = 'Forest 2011/'+fi
	workbook = xlrd.open_workbook(f_l)
	sheet = workbook.sheet_by_index(0)

	for r in range(1,sheet.nrows-1):
		#sheet1.write(r+cnt,0,f_l[41: ][ :-4])
		for c in range(0,sheet.ncols):
			data = sheet.cell_value(r,c)
			sheet1.write(r+b,c+1,data)
		cnt = cnt+1
	b = cnt



book.save("forest.xls")
	
