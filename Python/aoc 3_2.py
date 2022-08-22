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


oxygen_list = nl.copy()

len_oxygen = len(oxygen_list)

oxygen_count = defaultdict(list)

while len_oxygen != 1:

    for i in range(0,len(nl[0])):

        tl = list(map(lambda x : x[i] , oxygen_list))
        oxygen_count[i].update(Counter(tl))

    
    for key,value in oxygen_count.items():

        

        if len(set(c.values())) != 1:
            max_bit = max(c, key=c.get)
        else:
            max_bit = 1

        oxygen_list = list(filter(lambda x : x[key] == str(max_bit) , oxygen_list))


    len_oxygen = len(oxygen_list)


print(oxygen_list)

        # temp_max = [ [i, value[0].count(i)] for i in set(value[0]) ]

        # max_var : chr
        # max_val : int

        # for tm in temp_max:
            
        #     if tm[1] > max_val:
        #         max_var = tm[0]
        #         max_val = tm[1]

        

    


        # res_dic[key] = max(set(value[0]), key=value[0].count)
        # res_gamma += str(res_dic[key])










