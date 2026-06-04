import openpyxl as op

workbook = op.Workbook()
sheet = workbook.active

sheet ['A1'] = "ID"
sheet ['B1'] = "Last Name"
sheet['C1'] = "First Name"
sheet['D1'] = "Course"
sheet['E1'] = "Year"
sheet['F1'] = "Section"
sheet['G1'] = "Lab"
sheet['H1'] = "Day"
sheet['I1'] = "Time"




workbook.save("Menemedez_Database.xlsx")