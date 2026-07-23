nine = 69
print(type(nine))
s1 = str(nine)
s2 = float(nine)
print(s1, s2, type(s1), type(s2))

nin = 69.8
print(type(nin))
d1 = str(nin)
d2 = int(nin)
print(s1, s2, type(d1), type(d2))

a,b = "98","102.5"
print(type(a), type(b))
w, z = int(a), float(b)
print(type(w), type(z))

am = "1,'python',[2,['python',9],4],'java',['python',[56,78],'java',90]"
print(type(am))
y = list(am)
print(y, type(y))

af = "1,'python',[2,['python',9],4],'java',['python',[56,78],'java',90]"
h = tuple(af)
print(h, type(h))


num = [9,8,7,6,5,4,3,2,1]
print(type(num))
k = str(num)
print(k, type(k))

l = tuple(num)
print(l,type(l))


nums = (9,8,7,6,5,4,3,2,1)
i,j = str(nums), list(nums)
print(i,type(i))
print(j, type(j))
