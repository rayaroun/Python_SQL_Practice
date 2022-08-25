file1 = open("/Users/aroun/Documents/Python_SQL_Practice/python/bingo.txt", "r")
Lines = file1.readlines()
# nl = [ l[:-1] for l in Lines]

# # nl = Lines.split("\n\n")

# new_nl = [x.strip() for x in nl]

# numbers = []




# for i,item in enumerate(new_nl):
#     if i == 0:
#         numbers.append(item)

nl = (''.join(Lines)).split("\n\n")

numbers = [int(x) for x in nl[0].split(",")]

bingos = []

nl = nl[1:]

print(len(nl))
breakpoint

for i,item in enumerate(nl):
    ti = item.split("\n")
    
    tl = []
    
    print(i)
    
    for i in ti:
        i = i.strip()
        if i == '':
            continue
        else:
            i = i.replace("  "," ")
            tl.append([int(y) for y in i.split(" ")])
    
    bingos.append(tl)

print(bingos)

    