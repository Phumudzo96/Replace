#create a variable called sentence and assign a string to it
sentence = ("The!quick!brown!fox!jumps!over!the!lazy!dog!.")

#create another string that will be replacing the "!" in the string with a " "
sentence1 = (sentence.replace("!" ," "))
print(sentence1)

#create another variable that will make the string be in uppercase
sentence2 = (sentence1.upper())
print(sentence2)

#create another variable that will make the string be printed backwards
sentence3 = (sentence2[::-1])
print(sentence3)