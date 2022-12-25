name = "Ashutosh Gupta";
poem = """
A mountain and a squirell
had a quarell
and the former
called the later
little prig.
But replied
"""
sentence = 'Ram said, "I will go to the market today evening."'
# print(name);
# print(poem);
# print(sentence);

# for s in sentence:
#   print(s, end="");

# ____________________________________STRING SLICING____________________________________
string = 'Senorita';
#print(string[0:6]); #This will print the first 5 characters of the string.
#print(string[:6]); #We can also write the upper code like this.
#print(string[3:]); #This will print the string excluding the first 3 characters.
#print(string[0:-3]); #This is equivalent to print(string[0: len(string)-3]);
#print(string[-2:-3]); #This is equivalent to print(string[len(string)-3: len(string)-1]);

# ____________________________________STRING METHODS____________________________________
str = "welcome To Python course."
#print(len(string)); #This will print the length of the string.
print(str.upper()); #Converts all characters of upper case letters.
print(str.lower()); #Converts all characters of lower case letters.
print(str.rstrip('.')); #Removes the trailing characters if present in the string.
print(str.replace(" ", '_')); #Replaces all the occurrences of a string with the given string.
print(str.split(" ")); #Splits the while string.
print(str.capitalize()); #Capitalizes the first characters of the string and rest of the characters are converted to the smaller.
print(str.center(40)); #Adding 40 white-space characters in the begining.
print(str.count('e')); #Counting the occurence of e in the string.
print(str.endswith('.')) #Checking if the string ends with . or not.
print(str.startswith('wel')) #Will check if the string starts with wel.
print(str.endswith('To', 6, 10)) #Will check the occurrence of To in the given range.
print(str.find('elc')); #will find the index of the given substring.
print(str.isalnum()); #checks if the string is alpha-numeric or not.
print(str.islower()); #check if all the characters are in lower case letters.
print(str.isprintable()) #checks if all the characters of the string are printable or not.
print(str.isspace()) #checks if the string only contains the white space.
print(str.istitle()) #check if the characters are in title case in string.
print(str.swapcase()) #converts upper case to lower case and vice versa.
print(str.title()) #converts string into title case.