print("!!! Enter input filename+path. e.g.: /home/user/trojan.py")
filename = input("Enter input filename: ")
EICAR = open(filename, 'a')
a= '"""' + "\n"
b= 'X5O!P%@AP[4\PZX54(P^)7CC)7}$EICAR-STANDARD-ANTIVIRUS-TEST-FILE!$H+H*' + "\n"
EICAR.write(a) 
EICAR.write(b)
EICAR.write(a) 
EICAR.close()