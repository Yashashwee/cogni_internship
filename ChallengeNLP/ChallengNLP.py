import regex
import sys

n=len(sys.argv)
if n != 2:
    exit()

currency_reg='[$₹£][^\s][0-9]*[\.]{0,1}[0-9]*'
date_reg = '[0-9][0-9]\/[0-9][0-9]\/[0-9][0-9][0-9][0-9]|[0-9][0-9]\/[0-9][0-9]\/[0-9][0-9]'
card_reg =  '\s[4-9][4-9]*th|first|second|\s[a-zA-Z]+enth'
vowel_reg = '\s[aeiou][a-zA-Z]{3}\s|\s[AEIOU][a-zA-Z]{3}\s'

url = sys.argv[1]

with open(url,encoding='utf-8') as f:
    fileStr = f.read()
    print(regex.findall(date_reg,fileStr))
    print(regex.findall(currency_reg,fileStr))
    print(regex.findall(card_reg,fileStr))
    print(regex.findall(vowel_reg,fileStr))
