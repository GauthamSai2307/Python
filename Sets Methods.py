gau, tham = {1,2,3,8}, {} #creating a set with values and empty or without values inside it
print(type(gau), gau)

gau.update([9])
print(gau)

gau.add(10)
print(gau)

gau.remove(9)
print(gau)

gau.discard(10)
print(gau)

gaut = {99,1,26}
gaut.pop()
print(gaut)
