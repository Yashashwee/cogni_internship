import regex
import sys

#if we have less or more args we abandon ship!!
n=len(sys.argv)
if n != 2:
    print("Invalid number of args")
    exit()
url = sys.argv[1]

#defining our regexes
curr='[$₹£][^\s][0-9]*[\.]{0,1}[0-9]*'
date = '[0-2][0-9]\/[0-9][0-9]\/[0-9][0-9][0-9][0-9]|3[0-1]\/[0-9][0-9]\/[0-9][0-9][0-9][0-9]|[0-9][0-9]\/[0-9][0-9]\/[0-9][0-9]'
card =  '\s1st|2nd|3rd|\s[4-9]th|\s[1-9][0-9]*[4-9]th|first|second|third|fourth|fifth|sixth|seventh|eighth|nine?th|tenth|eleventh|twelfth|thirteenth|fourteenth|fifteenth|sixteenth|seventeenth|eighteenth|nineteenth|twentieth|thirtieth|fortieth|fiftieth|sixtieth|seventieth|eightieth|ninetieth|\s[a-zA-Z]+enth'
vowel = '\s[aeiou][a-zA-Z]{3}\s|\s[AEIOU][a-zA-Z]{3}\s'


with open(url,encoding='utf-8') as f:
    fileStr = f.read()
    print(regex.findall(date,fileStr))
    print(regex.findall(curr,fileStr))
    print(regex.findall(card,fileStr))
    print(regex.findall(vowel,fileStr))
