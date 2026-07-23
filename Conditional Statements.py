age = int(input("enter age : "))
if age >= 18:
    print(f"your age is {age} and you are eligible")
else :
    print(f"your age is {age} and you are not eligible")

year = int(input("enter age : "))
if year % 4 == 0 and year % 100 != 0 or year % 400 == 0:
    print(f"year is {year} and it is leap year")
else :
    print(f"year is {year} and it is not leap year")


sal = int(input("enter your salary per month : "))
if sal >= 50000 and sal < 74000:
    print(f"Your salary is {sal} and you can be promoted if you work hard")
elif sal >= 75000 and sal <200000:
    print(f"your salary is {sal} and you are in a good position")
else :
    print(f"you salary is {sal} and you need to work very hard to het promoted")

    
