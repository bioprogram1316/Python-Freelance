name = raw_input("What is your name?")
word = raw_input("Enter a word:")
pyg = 'ay'
print name

if word.isalpha():
    #if word contains only letters.
    print word[1:] + word[0] + pyg
    #print the word with the first letter missing plus the first letter plus ay.
else:
    print "Invalid Entry"
