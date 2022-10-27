import os
print("!!! Enter input filename+path. e.g.: /home/user/trojan.py")
print("----------------------------------------------------------")
filename = input("Enter input filename: ")
filename2 = input("Enter output filename: ")
homedir = os.path.expanduser("~")
f = open(filename, 'r')
s = f.read()
f.close()
bin(int.from_bytes(s.encode(), 'big'))
f = open(homedir+"/"+filename2, 'w')
ab = bin(int.from_bytes(s.encode(), 'big'))
b = "n = int(code, 2)" + "\n"
c = "n.to_bytes((n.bit_length() + 7) // 8, 'big').decode()"
a= '"""' + "\n"
aa= "code" +chr(92) + "\n"
aaa= chr(61)+chr(92) + "\n"
f.write(aa)
f.write(aaa)
f.write(a)
f.write(ab)
f.write(a)
f.write(b)
f.write("exec(")
f.write(c)
f.write(")")
f.write("#thanks for using Pyfuscator") 
f.close()
print("File created in: "+homedir)
