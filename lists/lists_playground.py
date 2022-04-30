#List
# 3 elements 
# 0 index, 0, 1, 2
# append only is able to be used to add 1 item to the end of a list

# This is an intro
# characters = ["a","b","c"]
# # print(characters[0])
# characters.append("d") 
# print(characters)

chilli_wishlist = ["igloo", "chicken", "donut toy", "cardboard box"]
chilli_wishlist.append('dig mat')
chilli_wishlist.extend(['kong', 'tennis ball', 'crocodile toy'])
chilli_wishlist.insert(1, 'peanut butter')
# print(chilli_wishlist)
chilli_wishlist.pop()
chilli_wishlist.pop(2)
chilli_wishlist.remove('kong')
# print(chilli_wishlist)
# indexing
# print(len(chilli_wishlist))
# print(chilli_wishlist[4])
# print(chilli_wishlist[0])
# print(chilli_wishlist[1])
# print(chilli_wishlist[-1])
# print(chilli_wishlist[0:2])
# print(chilli_wishlist[1:3])
# chilli_wishlist[1] = 'carrot'

if "tennis ball" in chilli_wishlist:
    print("Chilli would like a tennis ball.")
else: 
    print("Chilli doesn't feel like playing fetch.")

if len(chilli_wishlist > 8):
    print("chilli wants a lot of stuff!")