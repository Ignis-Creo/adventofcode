import re

nums = {
    'one':'1', 
    'two': '2',
    'three':'3',
    'four': '4',
    'five':'5',
    'six':'6',
    'seven':'7',
    'eight':'8',
    'nine':'9',
}
decoded = []

with open('day1data.txt', 'r') as f:
    for line in f:
        index_hash = {}
        for digit in re.finditer('\d', line):
            index_hash[digit.start()] = line[digit.start()]
        for key in nums.keys():
            if key in line:
                    index_hash[line.find(key)] = nums[key]
                    index_hash[line.rfind(key)] = nums[key]
                    
        sorted_indexs = sorted(list(index_hash))
        decoded.append(int(index_hash[sorted_indexs[0]] + index_hash[sorted_indexs[-1]]))
        
print(sum(decoded))