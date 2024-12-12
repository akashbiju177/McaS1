import csv

file_name='car.csv'
colums_to_read= ['Company', 'Car Model']
try:
    with open(file_name, newline='') as csvfile:
        reader=csv.DictReader(csvfile)
        missing_colums=[col for col in colums_to_read if col not in reader.fieldnames]
        if missing_colums:
            print(f"Missing colums in the file: {', '.join(missing_colums)}")
        else:
            print(", ".join(colums_to_read))
            for row in reader:
                print(", ".join(row[col] for col in colums_to_read))

except FileNotFoundError:
    print(f"Error: File '{file_name}' not found.")
except Exception as e:
    print(f"An error occured: {e}")