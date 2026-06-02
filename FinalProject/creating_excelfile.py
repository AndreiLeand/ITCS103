import openpyxl as op

workbook = op.Workbook()
sheet = workbook.active

sheet ['A1'] = "ID"
sheet ['B1'] = "Last Name"
sheet['C1'] = "First Name"
sheet['D1'] = "Middle Name"
sheet['E1'] = "Course"
sheet['F1'] = "Year"
sheet['G1'] = "Section"
sheet['H1'] = "Lab"
sheet['I1'] = "Day"
sheet['J1'] = "Time"




workbook.save("Menemedez_Database.xlsx")