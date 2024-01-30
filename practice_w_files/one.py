import csv 

file = open("practice_w_files/myfile.txt", "w")

L = ["This is a test",",", "Hmmmm", "Final Line?", "\n"]

file.write('Hello World!\n')
file.writelines(L)

