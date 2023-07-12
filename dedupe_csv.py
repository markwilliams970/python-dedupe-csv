import csv

def is_unique(this_id, list_of_ids):
  unique_test = True
  if this_id in list_of_ids:
    unique_test = False
  return unique_test

# Read input CSV and check if EmployeeID and SecondaryID fiels are both non-duplicates
# Output to unique output file if so

dict_template = {
  "EmployeeID": "I2F9J9NBQLC16Q8B",
  "DOB": "2019-12-20",
  "FirstName": "John",
  "LastName": "Doe",
  "Email": "john.doe@acme.com",
  "SecondaryID": "b83098ab50ca4af3a5ab1101d35b09a7",
  "Random": "8"
}

dict_template_keys = ['EmployeeID', 'DOB', 'FirstName', 'LastName', 'Email', 'SecondaryID', 'Random']

with open('samples_unique.csv', 'w') as output_file:
  output_writer = csv.DictWriter(output_file, dict_template_keys)
  output_writer.writeheader()
  with (open('samples_with_duplicates.csv', mode='r')) as csvfile:
    reader = csv.DictReader(csvfile)
    distinct_ids = []
    for row in reader:
      combination_id = row["EmployeeID"] + row["SecondaryID"]
      if (is_unique(combination_id, distinct_ids)):
        print("Unique combination id: " + combination_id + " found. Writing to file")
        distinct_ids.append(combination_id)
        output_writer.writerow(row)
      else:
        print("Combination id: " + combination_id + " already found. Not writing to file")
