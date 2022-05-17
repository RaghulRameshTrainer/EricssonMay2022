import re
'''
Regex Functions:
----------------
match -> will match the pattern only if it is in the begining of the line
search -> will match the pattern anywhere in the string , only one pattern will be matched
findall -> match every matches
sub
split
compile-finditer
'''
#
# mystr="pet:cat I love cat pet:dog I love dog"
# #result=re.match('pet:.{3}',mystr,re.I)
# #result=re.search('pet:...',mystr,re.I)
# result=re.findall('pet:...',mystr,re.I)
# print(result)
# print(re.sub('love','like',mystr))
# print(re.split(' ',mystr))

input_str="""
abcdefghijklmnopqrstuvwxyz
ABCDEFGHIJKLMNOPQRSTUVWXYZ
1234567890
!@#$%^&*()_+~
https://www.ericcson.com
http://www.ericcson.com
https://ericcson.com
https://www.ericcson.co.in

435-233-1223
324.535.2332
324_544_5544
443 554 5455

raghul_ramesh@gmail.com
raghulramesh@yahoo.com
Raghul.Ramesh@outlook.com
Raghul.Ramesh@hotmail.co.in

Ha HaHa
"""
#pattern=re.compile('https?://(www\.)?\w{8}\.com?(\.in)?')
#pattern=re.compile('\d{3}[\._\s]\d{3}[\._\s]\d{4}')
#pattern=re.compile('(\w+\.)?\w+@\w+\.com?(\.in)?')
pattern=re.compile(r'\bHa\b')
result=pattern.finditer(input_str)
for r in result:
    print(r.group())