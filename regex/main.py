import re

string = 'must be the best milo in the universe'
# print('milo' in string)
pattern = re.compile('the')

# exp = re.search('the', string)
a = pattern.search(string)
b = pattern.findall(string)

# needs the re.complile method to be full string for fullmath to return something
# ex: re.compile('must be the best milo in the universe')
c = pattern.fullmatch(string)

# matches the string but doenst care what happens afterwords
# ex: re.compile('must be the best milo in the universe ! skackalacka')
d = pattern.match(string)

# span - when the string occurs
# start- when the string starts
# end - when the string ends

print(d)

emailPattern = re.compile(r"(^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$)")
passwordRegex =  re.compile(r"[A-Za-z0-9$#%&@]{8,}\d")

email = "b@b.com"
password = 'SuperAdvent'

checher = emailPattern.search(email)
passChecker = passwordRegex.search(password)
print(checher)
print(passChecker)

