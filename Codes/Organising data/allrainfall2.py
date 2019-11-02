import xlrd
import xlwt
f_l = "morerain.xlsx"
workbook = xlrd.open_workbook(f_l)
fd = []
for i in range(0,19):
	sheet = workbook.sheet_by_index(i)
	#print sheet.nrows
	#print sheet.ncols	
	data = [[sheet.cell_value(r,c) for c in range(sheet.ncols)] for r in range(sheet.nrows)]
	fd.append(data)
	#print "-------"
#print data

book = xlwt.Workbook(encoding="utf-8")
cnt = 0

for i in range(0,19):
	sheet = workbook.sheet_by_index(i)
	c = sheet.ncols
	r = sheet.nrows
	for j in range(1,r-1):
		if fd[i][j][1] == 2011 or fd[i][j][1] == 2012 or fd[i][j][1] == 2013:
			print fd[i][j][0]+","+fd[i][j][1]+","+str(fd[i][j][2])+","+str(fd[i][j][15])
