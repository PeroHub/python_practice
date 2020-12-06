


integer = int(input("Enter positive interger: "))
if integer % 2 ==1:
    print("Weird")
if integer % 2 ==0 and integer in range(2, 5):
    print("Not Weird")
if integer % 2 ==0 and integer in range(6,20):
    print("Weird")
if integer % 2 and integer > 20:
    print("Not Weird")
