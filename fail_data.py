import csv
from io import TextIOWrapper
from zipfile import ZipFile

with open("fail_data", "w", newline="") as file:
    writer = csv.writer(file)
    writer.writerow(["fail_date", "model", "serial_number", \
        "hours_running"])
    with ZipFile("data_Q4_2019.zip") as zf:
        fileList = ZipFile.namelist(zf)
        for i in fileList:
            with zf.open(i, "r") as infile:
                reader = csv.reader(TextIOWrapper(infile))
                for row in reader:
                    if row[4] == "1":
                        writer.writerow([row[0], row[2], row[1], row[20]])


rest_files_list = ["data_Q1_2020.zip", "data_Q2_2020.zip", \
                    "data_Q3_2020.zip"]


with open("fail_data", "a", newline="") as file:
    for j in rest_files_list:
        writer = csv.writer(file)
        with ZipFile(j) as zf:
            fileList = ZipFile.namelist(zf)
            for i in fileList:
                with zf.open(i, "r") as infile:
                    reader = csv.reader(TextIOWrapper(infile))
                    for row in reader:
                        if row[4] == "1":
                            writer.writerow([row[0], row[2], row[1], row[20]])
