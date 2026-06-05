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

sheet ['A2'] = "1"
sheet ['B2'] = "Menemedez"
sheet['C2'] = "Andrei Leand"
sheet['D2'] = "BSIT"
sheet['E2'] = "1"
sheet['F2'] = "B"
sheet['G2'] = "CL3"
sheet['H2'] = "Monday"
sheet['I2'] = "07:00 - 08:30am"

sheet ['A3'] = "2"
sheet ['B3'] = "Pastorfide"
sheet['C3'] = "Oswald"
sheet['D3'] = "BSIT"
sheet['E3'] = "1"
sheet['F3'] = "B"
sheet['G3'] = "CL5"
sheet['H3'] = "Tuesday"
sheet['I3'] = "02:00 - 03:30pm"




workbook.save("Menemedez_Database.xlsx")