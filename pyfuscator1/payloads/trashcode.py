import random, os 
print("!!! Enter input filename+path. e.g.: /home/user/trojan.py")
print("----------------------------------------------------------")
filename = input("Enter input filename: ")
filename2 = input("Enter output filename: ") 
homedir = os.path.expanduser("~")
trash = 'abcdefghijklmnopqrstuvwxyz0123456789' 
lengh = random.randrange(5, 23) 
a = "#"+''.join(random.sample(trash, lengh))
with open(filename, 'r') as f:
	flines = [''.join([x.strip(), a, '\n']) for x in f]
with open(homedir+"/"+filename2, 'w') as f:
	f.writelines(flines)

print("File created in: "+homedir)