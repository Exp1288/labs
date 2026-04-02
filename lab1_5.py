import datetime
print("Program to determine age of a person if the year of birth is given")
year_of_birth = int(input("Enter the year of birth: "))
month_of_birth = int(input("Enter the month of birth (1-12): "))
day_of_birth = int(input("Enter the day of birth (1-31): "))
current_year = datetime.date.today().year
current_month = datetime.date.today().month
current_day = datetime.date.today().day
if (year_of_birth > current_year):
    print("Invalid year")
elif (month_of_birth > 12):
    print("Invaild month")
elif (day_of_birth > 31):
    print("Invalid day")
else:
    pass
year = current_year - year_of_birth - 1
month = (12 - month_of_birth) + current_month
day = (31 - day_of_birth) + current_day - 1
print("The age of the person is: ", year, "years", month, "months", day, "days")
