s = input("string to convert: ")
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
print('=====================================================================')
print('converted string: ')
print("exec("+ ''.join( l2 )[:-1] + ")")