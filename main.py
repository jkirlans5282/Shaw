inputString = input("Enter a string: ")
dictionarySpecial={'ch':'\U00010457','dg':'\U00010461','sh':'\U00010456','ou':'\U0001046C'}
dictionary = {'a':'\U00010468','b':'\U0001045A','c':'\U00010454',
			  'd':'\U0001045B','e':'\U00010467','f':'\U00010453',
			  'g':'\U0001045C','h':'\U00010463','i':'\U00010466',
			  'j':'\U00010462','k':'\U00010452','l':'\U00010464',
			  'm':'\U0001046B','n':'\U00010475','o':'\U00010469',
			  'p':'\U00010450','q':'q',         'r':'\U0001046E',
			  's':'\U00010455','t':'\U00010451','u':'\U0001046A',
			  'v':'\U0001045D','w':'\U00010458','x':'x'         ,
			  'y':'y'         ,'z':'\U0001045F'                 }

for key in dictionarySpecial:
	inputString = inputString.replace(key, dictionarySpecial[key])
for key in dictionary:
	inputString = inputString.replace(key, dictionary[key])
print(inputString)