# class CategoryTree:

#     def __init__(self):

#         self.cate = {}

#         pass

#     def add_category(self, category, parent):

#         # if (category in self.cate.values()) or (category in self.cate.keys()) :
#         #     raise KeyError("Value cannot be added once it has been added")
#         # elif parent and (parent not in self.cate.keys()):
#         #     raise KeyError("Value cannot be added once it has been added")



#         if (category) and (not parent):
#             self.cate[category] = []
            
#         # elif parent not in self.cate.keys():
#         #     self.cate[parent] = []
#         #     self.cate[parent].append(category)

#         else:
#             self.cate[parent].append(category)

#         pass

#     def get_children(self, parent):
#         return self.cate[parent]

# if __name__ == "__main__":
#     c = CategoryTree()
#     c.add_category('A', None)
#     c.add_category('B', 'A')
#     c.add_category('C', 'A')
#     c.add_category('X','J')

#     print(','.join(c.get_children('A') or []))



import collections

dic = collections.defaultdict(list)


dic[5] += 6

print(dic)



