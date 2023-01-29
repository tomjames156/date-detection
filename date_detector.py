# import re module
import re

# create a date regex in DD/MM/YYYY format
date_regex  = re.compile(r"^(\d{2})/(\d{2})/(\d{4})$")

# find a match
matche = date_regex.search("28/03/2023") # 03/11/20005 29/12/2007
print(matche.group())

# check if the stored dates are valid
day = int(match.group(1))
month = int(match.group(2))
year = int(match.group(3))

thirty_days = ["September", "April", "June", "November"]
# if any is not valid print it out