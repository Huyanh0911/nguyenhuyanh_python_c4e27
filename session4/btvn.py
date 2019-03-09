# inventory = {
#     'gold' : 500,
#     'pouch' : ['flint', 'twine', 'gemstone'],
#     'backpack' : ['xylophone', 'dagger', 'bedroll', 'bread loaf']
# }
# inventory["pocket"]=['seashell','strange berry','lint']
# inventory["backpack"].remove('dagger')
# inventory["gold"]=50,500
# print(inventory)
# ---------------------------------------------------------------------
prices = {
"banana": 4,
"apple": 2,
"orange": 1.5,
"pear": 3
}
stock = {
"banana": 6,
"apple": 0,
"orange": 32,
"pear": 15
}
# print("apple")
# print("prices:",prices['apple'])
# print("stock:",stock['apple'])
# print("pear")
# print("prices:",prices['pear'])
# print("stock:",stock['pear'])
total=0
for i in prices:
    t=prices[i]*stock[i]
    total=total+t
print(total)