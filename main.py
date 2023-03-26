string = "abcdefghi"
string = str.capitalize(string) # string = "Abcdefghi"
print(string)
string = str.upper(string) # string = "ABCDEFGHI"
print(string)
string = "abcdefghi"
print(string[:4])
string = "abcdefghi"
print(string.translate({ord(i): None for i in "acegi"}))


