import datetime

'''
%a  Weekday abbreviated name => Sun,Mon,...Sat
%A  Weekday Full name       => Sunday,Monday...
%w  Weekday as a decimal number => 0-Sunday, 1-Monday...6-Saturday
%d  Day of the month    => 01, 02, 03,....31

%b  Month's abbreviated Name    => Jan, Feb, Mar...
%B  Month's Full name         => January, February, March...
%m  Month is decimal number     =>01,02,...12

%y  Year in 2 digit         => 21,22,23,24,25...
%Y  Year in 4 digit         => 2021,2022, 2023, 2024, 2025....

%H  Hours in 24 hours format    =>00,01...23
%I  Hours in 12 hours format    => 00,01,...12
%p  AM|PM
%M  Minutes         => 00,01....59
%S  Seconds          => 00,01,...59
'''

# doj=datetime.date(2004,7,1)
# print("Year:",doj.year)
# print("Month:",doj.month)
# print("Day:",doj.day)

tday=datetime.date.today()
print("Today's date is:",tday)

now=datetime.datetime.now()
print("Today's date is:",now)

print(now.strftime("%A, %d %B %m/%d/%Y %I:%M %p"))

