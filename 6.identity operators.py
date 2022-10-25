# operatory tożsamości

strData = "test" # łańcuch znaków (Data-obiekt)

print( dir(strData) ) # dir - pokaże informacje o łańcuchu znaków

print( strData.upper() ) # upper - z łańcucha znaków - wyświetli - TEST
print(strData.title()) # test

intData = 10
print( dir(intData) ) # pokaże listę elementów z których możzemy korzystać

a = [1,2,3,4,5] # lista
b = a # zajmie to samo miejsce co a

# is - czy zmienna jest w tym samym miejscu pamięci
print( a is b ) # True
a.append(77) # append - dodajemy 77 do listy a
print(a) # wyświetli listę z 77
print(b) # wyświetli jw. to samo

# is not - czy zmienna jest w innym miejscu pamięci (czy nie w tym samym)
print( a is not b ) # False (czy a nie wskazuje na to samo miejsce co a)

c = [3,4,5] # nowa lista
print( a is c ) # False
print( a is not c ) # True
