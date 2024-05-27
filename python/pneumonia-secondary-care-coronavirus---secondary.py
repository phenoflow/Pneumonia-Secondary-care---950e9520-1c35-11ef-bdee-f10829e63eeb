# Eleftheria Vasileiou, Chukwuma Iwundu, Alex Williams, Clare MacRae, 2024.

import sys, csv, re

codes = [{"code":"CA40.1Y","system":"icd11"},{"code":"CA40.12","system":"icd11"},{"code":"CA40.11","system":"icd11"},{"code":"J10.8","system":"icd11"},{"code":"J11.8","system":"icd11"},{"code":"J10","system":"icd11"},{"code":"J11.0","system":"icd11"},{"code":"J12.1","system":"icd11"},{"code":"J10.0","system":"icd11"},{"code":"J09","system":"icd11"},{"code":"J10.1","system":"icd11"},{"code":"J12.2","system":"icd11"},{"code":"J11","system":"icd11"},{"code":"J11.1","system":"icd11"},{"code":"480.8","system":"icd11"},{"code":"480.3","system":"icd11"},{"code":"480.2","system":"icd11"},{"code":"480.1","system":"icd11"},{"code":"CA40.12","system":"icd11"},{"code":"CA40.1Y","system":"icd11"},{"code":"CA40.11","system":"icd11"},{"code":"J11.8","system":"icd11"},{"code":"J10.0","system":"icd11"},{"code":"J12.1","system":"icd11"},{"code":"J10","system":"icd11"},{"code":"J11.1","system":"icd11"},{"code":"J12.2","system":"icd11"},{"code":"J10.8","system":"icd11"},{"code":"J11.0","system":"icd11"},{"code":"J11","system":"icd11"},{"code":"J09","system":"icd11"},{"code":"J10.1","system":"icd11"},{"code":"480.2","system":"icd11"},{"code":"480.8","system":"icd11"},{"code":"480.3","system":"icd11"},{"code":"480.1","system":"icd11"}];
REQUIRED_CODES = 1;
with open(sys.argv[1], 'r') as file_in, open('pneumonia-secondary-care-potential-cases.csv', 'w', newline='') as file_out:
    csv_reader = csv.DictReader(file_in)
    csv_writer = csv.DictWriter(file_out, csv_reader.fieldnames + ["pneumonia-secondary-care-coronavirus---secondary-identified"])
    csv_writer.writeheader();
    codes_identified = 0;
    for row in csv_reader:
        newRow = row.copy();
        for cell in row:
            # Iterate cell lists (e.g. codes)
            for item in re.findall(r'\(([^,]*)\,', row[cell]):
                if(item in list(map(lambda code: code['code'], codes))): codes_identified+=1;
                if(codes_identified>=REQUIRED_CODES):
                    newRow["pneumonia-secondary-care-coronavirus---secondary-identified"] = "CASE";
                    break;
            if(codes_identified>=REQUIRED_CODES): break;
        if(codes_identified<REQUIRED_CODES):
            newRow["pneumonia-secondary-care-coronavirus---secondary-identified"] = "UNK";
        codes_identified=0;
        csv_writer.writerow(newRow)
