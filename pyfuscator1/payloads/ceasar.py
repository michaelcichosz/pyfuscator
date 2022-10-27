import os
print("!!! Enter input filename+path. e.g.: /home/user/trojan.py")
print("----------------------------------------------------------")
filename = input("Enter input filename: ")
filename2 = input("Enter output filename: ")
homedir = os.path.expanduser("~")
f = open(filename, 'r')
s = f.read()
f.close()
codelist = list(s)
 
cipher = 23 #int(input("Enter shifting value (1-26): "))
encstring = ''
 
for letter in codelist:
    point = ord(letter)
    if point > ord('z') or point < ord('a') :
        encstring += letter
    else:
        letter_position = point - ord('a')
        shifting_value = (letter_position + cipher) % 26
        shifted_letter = chr(ord('a') + shifting_value)
        encstring += shifted_letter
 
a= '"""' + "\n"
aa= "code" +chr(92) + "\n"
aaa= chr(61)+chr(92) + "\n"
b= str(encstring)
blah\
=\
"""
codelist = list(code)
cipher = 23
encstring = ''
 
for letter in codelist:
    point = ord(letter)
    if point > ord('z') or point < ord('a') :
        encstring += letter
    else:
        letter_position = point - ord('a')
        shifting_value = (letter_position - cipher) % 26
        shifted_letter = chr(ord('a') + shifting_value)
        encstring += shifted_letter
exec(str(encstring))
"""
f = open(homedir+"/"+filename2, 'w')
f.write(aa)
f.write(aaa)
f.write(a)
f.write(b)
f.write(a)
f.write(blah)
f.write("#thanks for using Pyfuscator") 
f.close()
print("File created in: "+homedir)