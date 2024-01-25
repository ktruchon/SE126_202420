import csv

#create some lists - one for EACH potential field in file
#1D PARALLEL LISTS
comp_type_list = []
manu_list = []
processor_list = []
ram_list = []
hdd_1_list = []
num_hdd_list = []
hdd_2_list = []
os_list = []
year_list = []




a = [
    'A', 
    'A', 
    'A'
    ]

b = ['B', 'B', 'B']
c = ['C', 'C', 'C']

#create an empty 2D LIST
#combines all of the parallel 1Ds - shorter, more efficient
text_file_list = []

with open("week3/lab2b.csv") as csvfile:

    file = csv.reader(csvfile)

    for rec in file:

        #2D list
        text_file_list.append(rec)
        #text_file_list.append(['D','DL','i5','08','001TB','1','W07','15'])


        #1D list

        comp_type_list.append(rec[0])
        manu_list.append(rec[1])
        processor_list.append(rec[2])
        ram_list.append(rec[3])
        hdd_1_list.append(rec[4])
        num_hdd_list.append(rec[5])

        if rec[5] == "1":
            hdd_2_list.append("   ")
            os_list.append(rec[6])
            year_list.append(rec[7])
        else:
            hdd_2_list.append(rec[6])
            os_list.append(rec[7])
            year_list.append(rec[8])
#--------------------
for i in range(0, len(comp_type_list)):
    print(f"{comp_type_list[i]}  {num_hdd_list[i]}  {year_list[i]}")


#2D list processing
print("2D LIST PRINT------------------------------")
for i in range(0, len(text_file_list)):

    print(f"{text_file_list[i]}")

    for x in range(0, len(text_file_list[i])):

        print(f"{text_file_list[i][x]}", end=" - ")

    #gives space for next list of data
    print()
