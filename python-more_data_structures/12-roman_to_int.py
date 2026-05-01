#!/usr/bin/python3
def roman_to_int(roman_string):
    if not isinstance(roman_string, str) or not roman_string:
        return 0
    sum = 0
    if "MMM" in roman_string:
        sum += 3000
        roman_string = roman_string.replace("MMM", "")
    if "MM" in roman_string:
        sum += 2000
        roman_string = roman_string.replace("MM", "")
    if "M" in roman_string:
        sum += 1000
        roman_string = roman_string.replace("M", "")
    if "CM" in roman_string:
        sum += 900
        roman_string = roman_string.replace("CM", "")
    if "DCCC" in roman_string:
        sum += 800
        roman_string = roman_string.replace("DCCC", "")
    if "DCC" in roman_string:
        sum += 700
        roman_string = roman_string.replace("DCC", "")
    if "DC" in roman_string:
        sum += 600
        roman_string = roman_string.replace("DC", "")
    if "D" in roman_string:
        sum += 500
        roman_string = roman_string.replace("D", "")
    if "CD" in roman_string:
        sum += 400
        roman_string = roman_string.replace("CD", "")
    if "CCC" in roman_string:
        sum += 300
        roman_string = roman_string.replace("CCC", "")
    if "CC" in roman_string:
        sum += 200
        roman_string = roman_string.replace("CC", "")
    if "C" in roman_string:
        sum += 100
        roman_string = roman_string.replace("C", "")
    if "XC" in roman_string:
        sum += 90
        roman_string = roman_string.replace("XC", "")
    if "LXXX" in roman_string:
        sum += 80
        roman_string = roman_string.replace("LXXX", "")
    if "LXX" in roman_string:
        sum += 70
        roman_string = roman_string.replace("LXX", "")
    if "LX" in roman_string:
        sum += 60
        roman_string = roman_string.replace("LX", "")
    if "L" in roman_string:
        sum += 50
        roman_string = roman_string.replace("L", "")
    if "XL" in roman_string:
        sum += 40
        roman_string = roman_string.replace("XL", "")
    if "XXX" in roman_string:
        sum += 30
        roman_string = roman_string.replace("XXX", "")
    if "XX" in roman_string:
        sum += 20
        roman_string = roman_string.replace("XX", "")
    if "IX" in roman_string:
        sum += 9
        roman_string = roman_string.replace("IX", "")
    if "X" in roman_string:
        sum += 10
        roman_string = roman_string.replace("X", "")
    if "VIII" in roman_string:
        sum += 8
        roman_string = roman_string.replace("VIII", "")
    if "VII" in roman_string:
        sum += 7
        roman_string = roman_string.replace("VII", "")
    if "VI" in roman_string:
        sum += 6
        roman_string = roman_string.replace("VI", "")
    if "IV" in roman_string:
        sum += 4
        roman_string = roman_string.replace("IV", "")
    if "V" in roman_string:
        sum += 5
        roman_string = roman_string.replace("V", "")
    if "III" in roman_string:
        sum += 3
        roman_string = roman_string.replace("III", "")
    if "II" in roman_string:
        sum += 2
        roman_string = roman_string.replace("II", "")
    if "I" in roman_string:
        sum += 1
        roman_string = roman_string.replace("I", "")
    return sum
