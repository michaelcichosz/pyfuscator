from file_read_backwards import FileReadBackwards
import os
print("!!! Enter input filename+path. e.g.: /home/user/trojan.py")
print("----------------------------------------------------------")
filename = input("Enter input filename: ")
filename2 = input("Enter output filename: ")
homedir = os.path.expanduser("~")
f = open(filename, 'rb')
s = f.read()
f.close()
a= '"""' + "\n"
aa= "code" +chr(92) + "\n"
aaa= chr(61)+chr(92) + "\n"
f = open(homedir+"/"+filename2, 'w')
f.write(aa)
f.write(aaa)
f.write(a)
f.close()
f = open(homedir+"/"+filename2, 'ab')
f.write(s[::-1]) 
f.close()


g = open(homedir+"/"+filename2, 'a')
b= "stringlength=len(code)" + "\n"
c= "codea=code[stringlength::-1]" + "\n"
d= "exec(codea.rstrip())" + "\n"
g.write(a)
g.write(b)
g.write(c)
g.write(d)
g.write("#thanks for using Pyfuscator") 
g.close()
print("File created in: "+homedir)
