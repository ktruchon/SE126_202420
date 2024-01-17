#W2D2 - Text File Opening Review + 1D Lists

import csv 

total_records = 0

#create empty lists for each field in the text file - base this on the maximum number of fields if working with a file with unever lists
#see addiitonal notes starting on line 31
fnames = []
lnames = []
favenums = []
faveanimals = []

with open("week2/demo/w2d2_demoTextFile.txt") as csvfile:
    #we must indent when connected to & reading the file

    file = csv.reader(csvfile)

    for rec in file:

        print(rec)

        #append field data to the appropriate list(s)
        fnames.append(rec[0])
        lnames.append(rec[1])
        favenums.append(int(rec[2]))

        #len() --> returns length of a structure (list);
        #the maximum length of rec is: 4

        #since the text file has uneven fields per record (not all rows in the file have the same amount of data values) we need to filter our .append() so those w/o fave animals still have a --- value appended and they do not "take" the next person's animal
        #this keeps all lists the same length! keeping all lists the same length ensures that specific list data (fname, lname, favenum, faveanimal) is still "connected" to its original row/record via index across each list
        # 
        # EX:  Josh M's data is found in text file row #7; this means that Josh's first name will be found in the fname list @ index 6 (-1 for starting at 0) -->fnames[6] -> 'Josh'
        #       the rest of Josh's info should stay in index 6 across all lists:
        #       lnames[6] -> M (Josh's last initial)
        #       favenums[6] -> 9 (Josh's favorite number)
        #       faveanimals[6] -> 'Capybara' (Josh's favorite animal)

        if len(rec) == 4:

            faveanimals.append(rec[3])
        else: #rec[3] does not exist
            faveanimals.append("---")


#process fnames + faveanimals list to display
for index in range(0, len(fnames)):
    print(f"{fnames[index]}'s fave animal is: {faveanimals[index]}")
