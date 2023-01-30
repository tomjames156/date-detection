# import re and pyperclip modules
import re, pyperclip

# create a date regex in DD/MM/YYYY format
date_regex  = re.compile(r"(\d{2})/(\d{2})/(\d{4})")

# find a match
date_match = date_regex.findall("29/02/100031/11/2000529/00/2007 28/03/2004")

thirty_day_months = ["September", "April", "June", "November"] # months with thirty days
months = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"]
valid_dates = ""


def is_valid_date(my_date):
    """This function checks if a date is valid"""

    # create variables for the day, month and year
    day = int(my_date[0])
    month = int(my_date[1])
    year = int(my_date[2])
    month_words = ""
    try:
        month_words = months[month - 1]
    except IndexError:
        print(f"{'/'.join(my_date)} is an invalid date")
        return "Month is out of range"

    avail_days = 0
    is_a_leap_year = is_leap_year(year)
    global valid_dates

    # Get total number of days for months apart from February
    if(month_words in thirty_day_months):
        avail_days = 30
    elif((month_words in months) and not(month_words in thirty_day_months)):
        avail_days = 31

    # Get total number of days in February based on if it is a leap year
    if(not(is_a_leap_year) and (month_words == "February")):
        avail_days = 28
    elif((is_a_leap_year) and (month_words == "February")):
        avail_days = 29

    # check if the days are correct according to the month
    if(day == 0 or day > avail_days):
        print(f"{'/'.join(my_date)} is an invalid date. Days are out of range")
    elif(not(month_words in months) or month == 0): # check if the month exists 
        print(f"{'/'.join(my_date)} is an invalid date. Month does not exist")
    elif(year == 0):
        print(f"{'/'.join(my_date)} is an invalid date. Year cannot be zero")
    else:
        valid_dates += f"{'/'.join(my_date)}\n"


def is_leap_year(test_year):
    """Checks if a year is a leap year"""
    if(((test_year % 4 == 0) and not(test_year % 100 == 0) )or (test_year % 400 == 0)):
        return True
    else: 
        return False

if not(date_match == []):
    ["" for date in date_match if(is_valid_date(date))]
    if(not(valid_dates == "")):
        no_of_valid_dates = len(valid_dates.split())
        pyperclip.copy(valid_dates.strip("\n"))
        print(f"{no_of_valid_dates} valid date(s) Copied to clipboard 📋")
    else:
        print("No valid dates were found 😢")
elif(date_match == []):
    print("No dates were found 😢")