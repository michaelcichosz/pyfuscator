import os, py_compile
print("!!! Enter input filename+path. e.g.: /home/user/trojan.py")
print("----------------------------------------------------------")
filename = input("Enter input filename: ")
py_compile.compile(filename)
