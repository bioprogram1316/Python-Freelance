f = open("linecut.txt", "r")

list_of_all_lines = f.readlines()

#this keeps track of which line we are reading currently, starting with line 0
line_number = 0

for line in list_of_all_lines:
    #if the line number is even, then print
    if line_number%2 == 0:
        print line
    #increase line number as we read
    line_number = line_number + 1
