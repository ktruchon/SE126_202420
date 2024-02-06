
import csv


fname = []
lname = []
test1 = []
test2 = []
test3 = []

#connect to file & read data into 1D lists

with open("week4/files/listPractice1.txt") as csvfile:

    file = csv.reader(csvfile)

    #come back and show print(file) later

    for rec in file:
        #store data from file fields to their respective list 
        #by PARALLEL - storing initial file record data at same posiiton (index) in each list --> use the same [INDEX] across each list to find "matching" data
        fname.append(rec[0])
        lname.append(rec[1])
        test1.append(int(rec[2])) #cast as int for math
        test2.append(int(rec[3]))
        test3.append(int(rec[4]))

#determine a randome int for index
import random
num = random.randint(0, 41)

print(num)

print(f"RANDOM INDEX: {num} which is line {num + 1} in your file.")
print(f"Here is your randome info: \n{fname[num]} {lname[num]} {test1[num]} {test1[num]} {test1[num]}")

