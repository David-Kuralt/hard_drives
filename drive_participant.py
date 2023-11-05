import csv

hd_data_list =[]
hd_fail_dict = {}
hd_nonfail_dict = {}

# create a dictionary with serial number as key and row as value for
# the failures, and put the rest of the rows in a list
with open("harddrive_data", "r", newline="") as from_file:
    reader = csv.reader(from_file)
    for row in reader:
        if row[0] == "": #identifies failure
            hd_fail_dict[row[2]] = row
        else:
            hd_data_list.append(row)

# create a dictionary with serial number as key and hours_running as value
# for hard drives that are still running on the last day of the observation
# period.
with open("period_end.csv", "r", newline="") as from_file:
    reader = csv.reader(from_file)
    for row in reader:
        if row[2] == "ST12000NM0008" or \
            row[2] == "TOSHIBA MG07ACA14TA": #these are hard drives still in
                                            #operation
            hd_nonfail_dict[row[1]] = row[20]

# for each row in data_list populate the hours_running field
# for rows of hard drives that failed, also populate the event_date field
for i in hd_data_list:
    bingo = i[2]
    if bingo in hd_fail_dict.keys():
        i[4] = hd_fail_dict[bingo][4]
        i[5] = hd_fail_dict[bingo][5]
    elif bingo in hd_nonfail_dict.keys():
        i[4] = hd_nonfail_dict[bingo]

# now we write the entries of hd_data_list to a csv file
with open("hd_data_clean", "w", newline="") as to_file:
    writer = csv.writer(to_file)
    for i in hd_data_list:
        writer.writerow(i)
