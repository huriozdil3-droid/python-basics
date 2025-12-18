import datetime
birth_year = int(input("birth year: "))
current_year = datetime.datetime.now().year
print("your age:" , current_year - birth_year)