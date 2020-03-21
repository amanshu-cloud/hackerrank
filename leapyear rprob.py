def is_leap(year):

    if year % 4 == 0 and year % 100 == 0 and year % 400 == 0:
        print(f"acc to gregorian calendar {year} is a leap year ")
        leap = True
    else :
        print(f"{year} is not a leap year")
        leap = False
    return leap

is_leap(1992)