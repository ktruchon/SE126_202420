#LAB 6B: SOLUTION FILE

#PROGRAM ROMPT:
#Write a Python program to assign passengers seats in an airplane.  Assume a small airplane with seat numbering as follows.
#                    Row					
#                    1	A	B		C	D
#                    2	A	B		C	D
#                    3	A	B		C	D
#                    4	A	B		C	D
#                    5	A	B		C	D
#                    6	A	B		C	D
#                    7	A	B		C	D
#The program should display the seat pattern, with an ‘X’ making the seats already assigned. For example, after seats 1A, 2B and 4C are taken the display should look like this:
#                    Row					
#                    1	X	B		C	D
#                    2	A	X		C	D
#                    3	A	B		C	D
#                    4	A	B		X	D
#                    5	A	B		C	D
#                    6	A	B		C	D
#                    7	A	B		C	D

#After displaying the seats available, the program prompts for the seat desired, the user types in a seat and then the display of available seats is updated.  This continues until all seats are filled or until the user signals that the program should end.  If a user types in a seat that is already assigned, the program should say that the seat is occupied and ask for another choice.
#       •	You must use functions that allows the user to enter the row and seat number.  The row should be asked for                  separately from the seat number (two inputs)
#       •	You must use a function that asks the user in they want to continue or stop. The function should only accept                an uppercase or lowercase y or n.



#VAIRABLE DICTIONARY
#~Variables~
#answer
#row_req            user's selection for the row they'd like to sit in, returned from row_choice (known in function as row_r)
#seat_req           user's selection for the seat they'd like to sit in, returned from seat_choice (known in function as seat_r)
#seat_c             loop control variable, used for seat choice confirmation
#answer             main loop control variable, used for user to reserve more than one seat
#confirm            used to control entering/exiting seat choice confirmation loop
#flag               flag variable used to determine if user selected an unreserved seat or not
#seat_sel           2-character string of where user has indivated they would like to reserve a seat
#~Lists~
#seatA              a list filled with seat A
#seatB              a list filled with seat B
#seatC              a list filled with seat C
#seatD              a list filled with seat D
#seats_selected     a list filled with all seats user has reserved during current session



#NOTES FOR THOSE READING THIS SOLUTION:
#There are some KEY observatons necessary to be successful with this lab
#   1. the seating chart displays just like a text file:
#
#               1   A   B       C   D
#               2   A   B       C   D
#               3   A   B       C   D
#               4   A   B       C   D
#               5   A   B       C   D
#               6   A   B       C   D
#               7   A   B       C   D
#      if approaching with the knowledge you have of text files, each FIELD becomes a LIST
#       this means you will have a list for: seatA, seatB, seatC, seatD
#
#   2. you are asking the user for two values: row choice, seat choice
#           * seat choice allows you to access the correct seat list
#           * row choice allows you to access the correct seat within that list
#   *KEY*
#           *if the user wants to sit in ROW 1 SEAT A, that will be the FIRST position of the seatA list
#           *what's the first position in computer programming? --> 0!
#                       How would you make 1 a 0? row choice - 1



#########################################################################################################################

#LIBRARY IMPORTS----------------------------------
from os import system, name 
  
#FUNCTIONS----------------------------------------

#A function that clears the console
def clear(): 
  
    # for windows 
    if name == 'nt': 
        _ = system('cls') 
  
    # for mac and linux(here, os.name is 'posix') 
    else: 
        _ = system('clear') 

#a function that gathers the user's row choice and returns this value

def row_choice():
    
    row_r = -1
    #working with try/except code blocks
    try:
        row_r = int(input("\t\t\tEnter the ROW you wish to sit in: "))
    
    except:
        # if an error is raised because the user didn;t provide a value that can be cast as an integer, it displays the below message
        print("\t\t\tROW MUST BE AN *INTEGER*")

    if row_r != -1:
        #above statement checks ot see if the user was able to enter an integer; when row_r is still -1, it means it has not been revalued ie the user has not provided a valid input and they hit the 'except' above
        # 
        # RECURSION: function calling itself below
        # when the user hasn't provided an appropriate value, we recall the function (like a loop!) 
        print(f"you entered: {row_r:.1f}")
        return row_choice()
    else:
        row_choice()






#a function that gathers the user's seat choice and returns this value
def seat_choice():

    seat_r = input("\t\t\tEnter the SEAT you wish to sit in: ")
    seat_r = seat_r.upper() #uppercase equivalent of what has been entered

    #checks for valid seat choice
    while seat_r != "A" and seat_r != "B" and seat_r != "C" and seat_r != "D":
        seat_r = input("\t\t\tEnter the SEAT you wish to sit in [A/B/C/D]: ")
        seat_r = seat_r.upper()

    #return seat_r value after validation; returns to wherever the call { seat_choice() } exists in base program
    return seat_r

#a function that asks the user in they want to continue or stop. The function should only accept                an uppercase or lowercase y or n.
def more_seats():

    ans = input("\n\n\t\t\tEnter Y to reserve another seat, N to exit: ")
    ans = ans.upper()

    #confirms answer is a valid value; traps user if it is not
    while ans != "Y" and ans != "N":
        print("\t\t\t\t**ERROR**") 
        ans = input("\t\t\tEnter Y to reserve another seat, N to exit: ")
        ans = ans.upper() 

    #function only returns when a valid y/n
    return ans


#BASE PROGRAM CODE--------------------------------------------------------------------------------------------------------


#initialize the seat lists
seatA = ['A','A','A','A','A','A','A']
seatB = ['B','B','B','B','B','B','B']
seatC = ['C','C','C','C','C','C','C']
seatD = ['D','D','D','D','D','D','D']

#i added this for final print to user of all seats reserved during the session
seats_selected = []

print("\t\t\t    AirDrogon ~ Valyria Bound Fight #4815")
print("\t\t\t -----------------------------------------")


answer = input("\t\t\tEnter 'Y' to see the seating chart & begin selecting seats: ")
answer = answer.upper()


while answer == "Y":
    

    seat_c = "Y"
    while seat_c == "Y":
        clear()
        #printing the seating chart
        print("\t\t\t    AirDrogon ~ Valyria Bound Fight #4815")
        print("\t\t\t -----------------------------------------")
        print("\t\t\t | \tROW # \t -   - \t\t -   - \t |")
        for i in range(0, 7):
        
            row = i + 1
            print("\t\t\t | \t", row, "\t", seatA[i], " ", seatB[i], "\t\t", seatC[i], " ", seatD[i], "\t |")

        print("\t\t\t ----------------------------------------- \n\n\n")

        row_req = row_choice() #return value has been validated in function
        print(f"here is row_req from main: {row_req}")

        seat_req = seat_choice() #return value has been validated in function

        #added confirmation to user; gives ability to change seat coice
        print("\n\t\t\tYou have requested the following seat:    {}. ".format(str(row_req) + seat_req))
        confirm = input("\t\t\tEnter Y to confirm or X to change: ")
        confirm = confirm.upper()

        #vaidation for confirm/change input values
        while confirm != "Y" and confirm != "X":
            confirm = input("\t\t\tEnter Y to confirm or X to change: ")
            confirm = confirm.upper()

        if confirm == "Y": #go through with seat choice
            seat_c = "x"

        else: #change seat choice
            seat_c == "y"
            clear()

    #flag variable created; when flag color changes to red, error message that seat is taken appears
    flag = "green"

    #user can only select A or B or C or D, so elif statement used to filter to only one possible choice
    if seat_req == "A": #seatA list
        if seatA[row_req - 1] != "X": #seatA in this row has not been reserved yet
            
            #change seatA at row choice value to X for reserved
            seatA[row_req - 1] = "X"

            #adds full seat to a variable for storage into an extra list which prints to user all of their reservations
            seat_sel = str(row_req) + seat_req
        else:
            #this will only set flag to ref when the seatA at row choice is already reserved (seatA[row_req - 1] == "X")
            flag = "red"

    elif seat_req == "B": #seatB list

        if seatB[row_req - 1] != "X":
            seatB[row_req - 1] = "X"
            seat_sel = str(row_req) + seat_req
        else:
            flag = "red"

    elif seat_req == "C": #seatC list

        if seatC[row_req - 1] != "X":
            seatC[row_req - 1] = "X"
            seat_sel = str(row_req) + seat_req
        else:
            flag = "red"
    else: #seatD list
        if seatD[row_req - 1] != "X":
            seatD[row_req - 1] = "X"
            seat_sel = str(row_req) + seat_req
        else:
            flag = "red"



    if flag == "red": #seat's taken
        print("\n\t\t\t\t**ERROR**") 
        print("\t\t\tSorry, seat's taken. Please choose another seat.")
        x = input("\t\t\tPress ENTER to continue to a new seat choice.") #input can be used to create a pause in console
    else:
        #adds seat to reservation list
        seats_selected.append(seat_sel)
    clear()

    #clear screen to reprint chart; this means the seating chart will stay in the same place

    print("\t\t\t    AirDrogon ~ Valyria Bound Fight #4815")
    print("\t\t\t -----------------------------------------")
    print("\t\t\t | \tROW # \t -   - \t\t -   - \t |")
    for i in range(0, 7):
        
        row = i + 1
        print("\t\t\t | \t", row, "\t", seatA[i], " ", seatB[i], "\t\t", seatC[i], " ", seatD[i], "\t |")

    print("\t\t\t ----------------------------------------- \n\n\n")

    answer = more_seats()

    clear()


#--------------------------------------
#printing the seating chart for final reservation review
print("\t\t\t    AirDrogon ~ Valyria Bound Fight #4815")
print("\t\t\t -----------------------------------------")
print("\t\t\t | \tROW # \t -   - \t\t -   - \t |")
for i in range(0, 7):
        
    row = i + 1
    print("\t\t\t | \t", row, "\t", seatA[i], " ", seatB[i], "\t\t", seatC[i], " ", seatD[i], "\t |")

print("\t\t\t ----------------------------------------- \n\n\n")



print("\n\n\n\t\t\tTo summarize, here are the seats you have reserved: ")
for i in range(0, len(seats_selected)):
    print("\t\t\t#", i + 1, " \t", seats_selected[i])

print("\n\n\n\t\t\tThank you for choosing AirDrogon. Enjoy your trip to Valyria!\n\n\n\n\n")