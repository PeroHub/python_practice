# A scalene triangle is a triangle in which all three sides have different lengths
# An isosceles triangle is a triangle that has two sides of equal length. 
# An equilateral triangle is a triangle in which all three sides have the same 

a = int(input("Enter the length of a = "))
b = int(input("Enter the length of b = "))
c = int(input("Enter the length of c = "))

if a != b and b != c and a != c:
    print("This is an scalene triangle ")

# if a is equal to b but c is not equal to either a or b....same process repeat.6

elif a == b and c != a or c != b and b == c and a != b or a != c and c == a and b != c or b != a:
    print("This is an isosceles triangle") 

elif  a == b and b == c and a == b:
    print("This is an equilateral triangle ")  

else:
    print("I do not know what the hell you are doing")         