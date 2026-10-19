# 1. tuple ke total elements kaise find kare ?

t = (10,20,30,40,50)
print(len(t))

# 2. specific value kitni baar aatib hai

# my = (10,20,30,10,20,30,20,10)
# print(my.count(10))

# 3. elements ka first index kaise find kare

# my = (10,20,30,40)
# print(my.index(20))

# 4. tuple ko indivdual variables me unpack kare

# my = (10,20,30)
# a,b,c = my
# print(a)
# print(b)
# print(c)

# 5. slicing se tuple reverse kare

# my = (10,20,30,40)
# print(my[::-1])

# 6. do tuple ko concatenate kare

# my1 = (10,20,30,40)
# my2 = (50,60,70,80)
# my3 = my1+my2

# print(my3)

# 7. tuple ke elements ko 3 times repeat kare

# my = (10,20,30)
# print (my*3)

# 8. sirf first 3 elements ka tuple niakle

# my = (10,20,30,40,50)
# print(my[:3])

# 9. cheak kare ki item tuple me exits katra hai

# my = (10,20,30,40,50)
# print(60 in my)

# 10.kya tuple banne ke baad element change/add/remove kar sakte hain? nahi

# my = (10,20,30,40,50)
# my[0] = 30

a = (1,2,3,4, 'hello', "jaipu",[1,2])
i = 0
while i < len(a):
  print(a[i])
  i +=1