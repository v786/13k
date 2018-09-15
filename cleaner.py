import re

raw = open("test.txt", "r")
mystring = raw.read()
result = []
final = ''
cleanString = re.sub(r'[-()\"#/@;:<>{}`+=~|!?,a-zA-Z]+[0-9]+\.*[0-9]*', '', mystring)
raw.close()
print(cleanString)
raw = open("result.txt", "a")
raw.write(final)

raw.close()
