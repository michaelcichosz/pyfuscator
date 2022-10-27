import os
print("!!! Enter input filename+path. e.g.: /home/user/trojan.py")
print("----------------------------------------------------------")
filename = input("Enter input filename: ")
filename2 = input("Enter output filename: ")
homedir = os.path.expanduser("~")
f = open(filename, 'r')
s = f.read()
f.close()
lst=[]
for letter in s:
	lst.append(letter)
print(lst)
aa= "string=" #+ "\n"
f = open(homedir+"/"+filename2, 'w')
f.write(aa)
f.close()

f = open(homedir+"/"+filename2, 'a')
f.write(str(lst))
f.close()

g = open(homedir+"/"+filename2, 'a+')
a= "\n"
b= "def convert(string):" + "\n"
c='	space=""' + "\n"
d="	return(space.join(string))" + "\n"
e="exec(convert(string))"
g.write(a)
g.write(b)
g.write(c)
g.write(d) 
g.write(e) 
g.write("#thanks for using Pyfuscator") 
g.close()
print("File created in: "+homedir)