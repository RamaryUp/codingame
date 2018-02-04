# Codingame challenge
# Name : Laser and mirrors
# Category : Community puzzles
# URL : https://www.codingame.com/training/community/these-romans-are-crazy!

'''
You are given 2 expressions representing 2 numbers written in roman numerals.
You have to provide the result of the sum of these 2 numbers, also in roman numerals.

I has a value of 1 (maximum 3 in a row)
V has a value of 5 (maximum 1 in a row)
X has a value of 10 (maximum 3 in a row)
L has a value of 50 (maximum 1 in a row)
C has a value of 100 (maximum 3 in a row)
D has a value of 500 (maximum 1 in a row)
M has a value of 1000 (maximum 4 in a row)

The character I just before an V or X has a value of -1 (example IX equals 9)
The character X just before an L or C has a value of -10 (example XL equals 40)
The character C just before an D or M has a value of -100 (example CM equals 900)
Input
Line 1 : Rom1 (the 1st number in roman numerals)
Line 2 : Rom2 (the 2nd number in roman numerals)
Output
The result of Rom1 + Rom2 written in roman numerals
Constraints
1 ≤ Rom1 ≤ 4999
1 ≤ Rom2 ≤ 4999
1 ≤ Rom1 + Rom2 ≤ 4999
Example
Input
VI
VII
Output
XIII
'''

def create_roman_dict(integer_dict):
    roman_dict = {}
    for key in integer_dict.keys():
        val = integer_dict[key]
        roman_dict[val] = key
    return roman_dict

def roman_to_integer(rom, roman_dict):
    i = 0
    val = 0
    while True:
        if len(rom[i:]) == 0:
            return val
        
        if len(rom[i:]) >= 2:
            subtext = rom[i:i+2]
            if subtext in roman_dict:
                val += roman_dict[subtext]
                i += 2
                continue

        subtext = rom[i:i+1]
        if subtext in roman_dict:
            val += roman_dict[subtext]
            i += 1
            continue
        raise Exception(subtext + ' not in roman_dict')
        
            
def integer_to_roman(number, integer_dict):
    rom = ''
    for i, digit in enumerate(str(number)[::-1]):
        if digit == 0:
            # 0 is not represented i in roman numbers
            continue
        key = (10 ** i) * int(digit)
        rom = integer_dict[int(key)] + rom
    
    return rom


dict_units = {0:'', 1:'I', 2:'II', 3:'III', 4:'IV', 5:'V', 6:'VI', 7:'VII', 8:'VIII', 9:'IX'}
dict_tens = {10:'X', 20:'XX', 30:'XXX', 40:'XL', 50:'L', 60:'LX', 70:'LXX', 80:'LXXX', 90:'XC'}
dict_hundreds = {100:'C', 200:'CC', 300:'CCC', 400:'CD', 500:'D', 600:'DC', 700:'DCC', 800:'DCCC', 900:'CM'}
dict_thousands= {1000:'M', 2000:'MM', 3000:'MMM', 4000:'MMMM'}

int_dict={**dict_units, **dict_tens, **dict_hundreds, **dict_thousands}
rom_dict = create_roman_dict(int_dict)


rom_1 = input()
rom_2 = input()

int_1 = roman_to_integer(rom_1, rom_dict)
int_2 = roman_to_integer(rom_2, rom_dict)

int_total = int_1 + int_2
rom_total = integer_to_roman(int_total, int_dict)

print(rom_total)