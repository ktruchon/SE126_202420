import csv 

#create 1D lists [will be parallel to each other]
#base lists on fields in file 

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
#disconnected from file ---------------------
'''
#PROCESS the lists --> for loop
print(f"{'FIRST':12} \t {'LAST':12} \t {'TEST1'} \t {'TEST2'} \t {'TEST3'}")
print("---------------------------------------------------------------------------------")
#display the file data
for i in range(0, len(fname)): 
    #len() --> returns LENGTH of (item) -> for lists, it is the # of items in the list

    print(f"{fname[i]:12} \t {lname[i]:12} \t {test1[i]} \t {test2[i]} \t {test3[i]}")
print("---------------------------------------------------------------------------------")
'''

#calculate and store each student's AVERAGE TEST SCORE
avg = 0
total_count = 0
average = []

for i in range(0, len(test1)):
    #calculate avg for student 
    avg = (test1[i] + test2[i] + test3[i]) / 3

    #append this avg to the average[]
    average.append(avg)
'''
#display student's fname and test average
print(f"{'FIRST'}\t{'AVERAGE'}")
for i in range(0, len(fname)):
    print(f"{fname[i]:12} \t {average[i]:8.1f}")

#SEQUENTIAL SEARCH - "in sequence" --> from beginning THROUGH the end
low_name = ""
low_avg = 100 #start with highest value to drop to find lowest

for i in range(0, len(average)):

    #determine if current average is lower than current low_avg
    if average[i] < low_avg:

        low_avg = average[i] #current average is lower, so becomes new low value 
        low_name = fname[i]
#DISPLAY: total students in file
print(f"STUDENTS IN FILE: {len(fname)}")
print(f"LOWEST AVERAGE: {low_name} - {low_avg:.1f}")
'''
#----2D LISTS---------------------------------------------------------
print(f"\n\n---2D LIST DISPLAY----------------------------------------")
#use your 1D parallel lists to populate a new, 2D list
#HINT: the 2D list is a list ... populated with lists 8D
all_students = []


for i in range(0, len(fname)):

    #add each student's data to their (index) place in the all_students[]
    all_students.append([fname[i], lname[i], test1[i], test2[i], test3[i], average[i]])
'''

#display the 2D list to the console - for now, just get the lists to display ie ['Floyd','Eastham','100','85','93']
for i in range(0, len(all_students)):
    print(f"{all_students[i]}")
'''
print(f"----2D LISTS - INDIV. VALUES!----------------------------------")
print(f"{'FIRST':12} \t {'LAST':12} \t {'TEST1'} \t {'TEST2'} \t {'TEST3'}, {'AVERAGE'}")
print("--------------------------------------------------------------")
#display the 2D list to the console where each value for each list appears as a value (and not a list item)
for i in range(0, len(all_students)):
    #we have lists within a list - outter for handles main list (all_students)
    for x in range(0, len(all_students[i])):
        #inner for handles each value found at current list (all_students[i])
        if type(all_students[i][x]) == str:
         print(f"{all_students[i][x]:12}", end="")
        else:
           print(f"{all_students[i][x]:7.1f}", end="") 

    #include an extra empty print() to cancel the interior print's end=""
    print()