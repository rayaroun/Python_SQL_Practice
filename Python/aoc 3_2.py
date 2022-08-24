"""

life support rating     =       oxygen generator rating * co2 scrubber rating


using the binary number list :

    consider just th3e first bit

        keep only numbers that are selected through the criteria , remove others

        if only one number left, stop -  RATING VALUE obtained

        otherwise repeat with moving to the next bit


BIT CRITERIA

    OXYGEN GENERATOR - find most common bit , keep only numbers that have that bit in that positions
                       if equal number of count, then pick 1
    
    CO2 RATING       - find least comon, keep only numbers that have that bit in that position
                       if equal number of count, then pick 0
      



00100
11110
10110
10111
10101
01111
00111
11100
10000
11001
00010
01010



"""

"""
Idea 1 - 

create a new list with the same data 

while length of the new list is > 1

    do 
        for each bit 
            find the max occurance 
            remove the other numbers from the new list



"""


from collections import Counter, defaultdict


file1 = open("/Users/aroun/Documents/Python_SQL_Practice/python/binary.txt", "r")
Lines = file1.readlines()
nl = [ l[:-1] for l in Lines]


oxygen_list, carbon_rating = nl.copy(), nl.copy()

len_oxygen = len(oxygen_list)

oxygen_count = defaultdict(dict)

for i in range(0,len(nl[0])):

    tl = list(map(lambda x : x[i] , oxygen_list))

    max_bit = None

    # print(f' key is {i}')

    # print(set(Counter(tl).items()))

    if len(set(Counter(tl).values())) != 1:
        max_bit = max(Counter(tl), key=Counter(tl).get)
    else:
        max_bit = 1

    # print(max_bit)

    oxygen_list = list(filter(lambda x : x[i] == str(max_bit) , oxygen_list))

    # print(f'oxygen list {oxygen_list} ')
    # len_oxygen = len(oxygen_list)

    if len(oxygen_list) == 1:
        break
    

print(oxygen_list)
print(int(oxygen_list[0],2))

for i in range(0,len(nl[0])):

    tl = list(map(lambda x : x[i] , carbon_rating))

    min_bit = None

    # print(f' key is {i}')

    # print(set(Counter(tl).items()))

    if len(set(Counter(tl).values())) != 1:
        min_bit = min(Counter(tl), key=Counter(tl).get)
    else:
        min_bit = 0

    # print(max_bit)

    carbon_rating = list(filter(lambda x : x[i] == str(min_bit) , carbon_rating))

    # print(f'oxygen list {oxygen_list} ')
    # len_oxygen = len(oxygen_list)

    if len(carbon_rating) == 1:
        break

print(carbon_rating)
print(int(carbon_rating[0],2))
