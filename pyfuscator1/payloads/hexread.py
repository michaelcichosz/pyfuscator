import os
print("!!! Enter input filename+path. e.g.: /home/user/trojan.py")
print("----------------------------------------------------------")
filename = input("Enter input filename: ")
filename2 = input("Enter output filename: ")
homedir = os.path.expanduser("~")
infile = open(filename, 'rb')
outfile = open(homedir+"/"+filename2, 'w')
i = 1
for line in infile:
	a = "exec(bytearray.fromhex('"
	b = line.rstrip().hex()
	c = "').decode())\n"
	print(a+b+c)
	outfile.write(a+b+c)
	i = i + 1
	
infile.close()
outfile.write("#thanks for using Pyfuscator") 
outfile.close()
print("File created in: "+homedir)