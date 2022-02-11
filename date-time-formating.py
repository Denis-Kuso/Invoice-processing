import datetime

test_string2 = '11 November 2020 - 15 November 2020'

# Split date by hypen
separator = ' - '
testing_string = test_string2.split(sep = separator)
testing_strings = []
# Convert each string in list into a datetime object
for date in testing_string:
    testing_strings.append(datetime.datetime.strptime(date, '%d %B %Y').date())
# Stich two dates back into one string
formated_string = str(testing_strings[0]) + separator + str(testing_strings[1])
print(formated_string)
