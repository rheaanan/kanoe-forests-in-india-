import xlrd
import xlwt
f_l = "imd_district-wise_rainfalldata_2004-2010.xls"
workbook = xlrd.open_workbook(f_l)
fd = []
for i in range(1,36):
	sheet = workbook.sheet_by_index(i)
	#print sheet.nrows
	#print sheet.ncols	
	data = [[sheet.cell_value(r,c) for c in range(sheet.ncols)] for r in range(sheet.nrows)]
	fd.append(data)
	#print "-------"

book = xlwt.Workbook(encoding="utf-8")
cnt = 0
sheet1 = book.add_sheet("Sheet 1",cell_overwrite_ok=True)
for i in range(1,36):
	sheet = workbook.sheet_by_index(i)
	c = sheet.ncols
	r = sheet.nrows
	for j in range(r-1):
		if fd[i-1][j][2] == 2010 or fd[i-1][j][2] == 2007 or fd[i-1][j][2] == 2008 or fd[i-1][j][2] == 2009:
			print fd[i-1][j][0]+","+fd[i-1][j][1]+","+str(fd[i-1][j][2])+","+str(fd[i-1][j][15])
			

book.save("intermediate.xls")
