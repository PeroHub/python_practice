from datetime import datetime

def calculateAge(birthyear):
    """ A function that accept user year born and calculate what their age will be in a certain year """

    # Get the present year
    year = datetime.datetime.now().year

    # difference between present year and the year of birth
    your_age = year - year_of_birth
    return your_age

year_of_birth = int(input("Please enter the year you were born here: ")) 
birthyear = year_of_birth
print(calculateAge(birthyear))
