import itertools
f = open("linecut.txt", "r")

#Read the file and puts each line in a list
list_of_all_lines = f.readlines()
#Picking the odd lines and put them in different list
list_of_odd_lines = itertools.islice(list_of_all_lines,0,None,2)

for line in list_of_odd_lines:
    print line

f.close()
