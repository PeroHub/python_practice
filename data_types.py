i = 4
d = 4.0
s = 'HackerRank '
# Declare second integer, double, and String variables.

# Read and save an integer, double, and String to your variables.

# Print the sum of both integer variables on a new line.

# Print the sum of the double variables on a new line.

# Concatenate and print the String variables on a new line
# The 's' variable above should be printed first.
while True:
    try:
        var1 = int(input("Enter integer value here: "))
    
    except ValueError:
        print("oops! That was no integer number. Try again")
        
        

    try:
        var2 = float(input("Enter float value here: "))
    except ValueError:
        print("oops! That was no float number. Try again")  

var3 = input("Enter string value here: ")


print(i + var1)
print(d + var2)
print(s + var3)