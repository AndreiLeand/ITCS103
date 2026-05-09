import openpyxl
from datetime import datetime

def main():
    current_year = datetime.now().year
    
    records = []
    
    print("--- Favorite People Recorder ---")
    print("Please enter information for 3 favorite people.\n")

    for i in range(1, 4):
        print(f"Person {i}:")
        first_name = input("  First Name: ").strip()
        last_name = input("  Last Name: ").strip()
        
        while True:
            try:
                birth_year_str = input("  Birth Year: ").strip()
                birth_year = int(birth_year_str)
                if birth_year < 1900 or birth_year > current_year:
                    print(f"  Please enter a valid birth year between 1900 and {current_year}.")
                else:
                    break
            except ValueError:
                print("  Invalid input. Please enter a numeric year.")

        age = current_year - birth_year

        person_id = i
        
        record = {
            "ID": person_id,
            "First Name": first_name,
            "Last Name": last_name,
            "Birth Year": birth_year,
            "Age": age
        }
        records.append(record)
        print() 

    wb = openpyxl.Workbook()
    ws = wb.active
    ws.title = "Favorite People"

    headers = ["ID", "First Name", "Last Name", "Birth Year", "Age"]
    ws.append(headers)

    for record in records:
        ws.append([
            record["ID"],
            record["First Name"],
            record["Last Name"],
            record["Birth Year"],
            record["Age"]
        ])

    excel_filename = "favorite_people.xlsx"
    wb.save(excel_filename)
    print(f"Data successfully saved to '{excel_filename}'.\n")

    print("--- Saved Records ---")
    print(f"{'ID':<5} {'First Name':<15} {'Last Name':<15} {'Birth Year':<12} {'Age':<5}")
    print("-" * 55)
    
    for record in records:
        print(f"{record['ID']:<5} {record['First Name']:<15} {record['Last Name']:<15} {record['Birth Year']:<12} {record['Age']:<5}")

main()