import re
# input1 = ['1abc2',
# 'pqr3stu8vwx',
# 'a1b2c3d4e5f',
# 'treb7uchet']

decoded = []
with open('day1data.txt', 'r') as f:
    for line in f:
        digits = re.findall('\d', line)
        decoded.append(int(digits[0] + digits[-1]))
print(sum(decoded))