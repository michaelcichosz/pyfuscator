import os
print("!!! Enter input filename+path. e.g.: /home/user/trojan.py")
print("----------------------------------------------------------")
filename = input("Enter input filename: ")
filename2 = input("Enter output filename: ")
homedir = os.path.expanduser("~")
f = open(filename, 'r')
s = f.read()
f.close()
l1 = []
a = 'chr('
b = ')+'
l2 = []
counter = 0
for c in s:
    l1.append( ord( c ) )
    l2.append( a )
    l2.append( str( l1[ counter ] ) )
    l2.append( b )
    counter += 1
print('===================')
print('converted string: ')
print(( ''.join( l2 )[:-1] ))

f = open(homedir+"/"+filename2, 'w')
f.write("exec(")
f.write(str( ''.join( l2 )[:-1] ))
f.write(")")
f.write("#thanks for using Pyfuscator") 
f.close()
print("File created in: "+homedir)