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

#You must use functions that allows the user to enter the row and seat number.  The row should be asked for separately from the seat number (two inputs)
def get_row():
    '''this function gets the row choice (1-7) user would like to sit in, checks that it is within the appropriate range, and returns it to the base program'''

    row_r = -1 #sets row to something < 1 that is out of our acceptable range

    #usually we would just use a loop to check for valid row choice
    #while row_r < 1 or row_r > 7: 
    #    row_r = int(input("\t\t\tEnter the ROW you wish to sit in [1-7]: "))

    #but what if our user supplies a string?
    #When an error occurs, or exception as we call it, Python will normally stop and generate an error message.These exceptions can be handled using the try statement:
    #more here: https://www.w3schools.com/python/python_try_except.asp 
    
    while row_r < 1 or row_r > 7:
        #working with try/except code blocks
        try:
            row_r = int(input("\t\t\tEnter the ROW you wish to sit in [1-7]: "))
        
        except:
            # if an error is raised because the user didn;t provide a value that can be cast as an integer, it displays the below message
            print("\t\t\tROW MUST BE AN *INTEGER*")
    return row_r


def get_seat():
    '''this function gets the seat choice (A/B/C/D) the user would like to sit in, checks that it is within the appropriate range, and returns it to the base program '''

    acceptable_seats = ["A", "B", "C", "D"]

    seat_r = input("\t\t\tEnter the SEAT you wish to sit in: ").upper() 
    #uppercase equivalent of what has been entered

    #checks for valid seat choice
    while seat_r not in acceptable_seats:
        seat_r = input("\t\t\tEnter the SEAT you wish to sit in [A/B/C/D]: ").upper() 

    #while seat_r != "A" and seat_r != "B" and seat_r != "C" and seat_r != "D":
    #    seat_r = input("\t\t\tEnter the SEAT you wish to sit in [A/B/C/D]: ")
    #    seat_r = seat_r.upper()

    #return seat_r value after validation; returns to wherever the call { seat_choice() } exists in base program
    return seat_r





#You must use a function that asks the user in they want to continue or stop. The function should only accept an uppercase or lowercase y or n.
def more_seats():
    '''this function asks the user if they would like to reserve another seat, checks that the value is an uppercase y or n, and then returns the value back to the main program'''


#BASE (MAIN) PROGRAM CODE---------------------------------------------------------------------------------------


#initialize the seat lists
seatA = ['A','A','A','A','A','A','A']
seatB = ['B','B','B','B','B','B','B']
seatC = ['C','C','C','C','C','C','C']
seatD = ['D','D','D','D','D','D','D']

#i added this for final print to user of all seats reserved during the session
seats_selected = []

print("\t\t\t    AirDrogon ~ Valyria Bound Fight #4815")
print("\t\t\t -----------------------------------------")


answer = input("\t\t\tEnter 'Y' to see the seating chart & begin selecting seats: ").upper()

while answer == "Y":
    #clear()
    #bring back the clear() when youre ready to have the seating chart "refresh" in real time! 

    #printing the seating chart
    print("\t\t\t    AirDrogon ~ Valyria Bound Fight #4815")
    print("\t\t\t -----------------------------------------")
    print("\t\t\t | \tROW # \t -   - \t\t -   - \t |")
    for i in range(0, 7):
        
        row = i + 1
        print("\t\t\t | \t", i + 1, "\t", seatA[i], " ", seatB[i], "\t\t", seatC[i], " ", seatD[i], "\t |")

    print("\t\t\t ----------------------------------------- \n\n\n")

    row_req = get_row() #return value has been validated in function
    seat_req = get_seat() #return value has been validated in function

    print(f"You have chosen: ROW:{row_req} SEAT: {seat_req}")

    #row_req is +1 of the index of where theyd like to sit
    #so you could check the seat value first to isolate which list you need

    if seat_req == "A":
        #seatA list 
        #once you are in the right list, now check to see if where they want to sit is available(!= "X")
        if seatA[row_req - 1] != "X":
            #when the seat isn't taken, place your X!
            seatA[row_req - 1] = "X"
        else:
            #otherwise, alert them!
            print(f"\t\t\tSorry but, {row_req}{seat_req} is already taken.\n\n")


    answer = input("\n\t\t\tWould you like to select another seat?").upper()

#for final confirmation challenge:
#display to the user all of the seats they selected, IN ORDER of front->back of plane :]