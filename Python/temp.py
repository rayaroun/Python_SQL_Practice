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



# import collections

# dic = collections.defaultdict(list)


# dic[5] += 6

# print(dic)



# Python Program to find the size of binary tree
 
# A binary tree node
# class Node:
 
#     # Constructor to create a new node
#     def __init__(self, data):
#         self.data = data
#         self.left = None
#         self.right = None
 
# # Computes the number of nodes in tree
# def size(node):
#     if node is None:
#         return 0
#     else:
#         return (size(node.left)+ 1 + size(node.right))
 
 
# # Driver program to test above function
# root = Node(1)
# root.left = Node(2)
# root.right = Node(3)
# root.left.left  = Node(4)
# root.left.right = Node(5)
 
# print("Size of the tree is %d" %(size(root)))



# st = ""
# st+="abc"

# print(st+"xyz")



ls = [1,2,3,4,5]

test0 = True if ls[:0] else False

test1 = True if ls[len(ls):] else False

print(test0, test1)