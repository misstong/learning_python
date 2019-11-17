import heapq

nums = [1, 8, 2, 23, 7, -4, 18, 23, 42, 37, 2]
print(heapq.nlargest(3,nums))
print(heapq.nsmallest(3,nums))


portfolio = [
    {'name':'a','age':12},
    {'name':'b','age':14},
    {'name':'c','age':15}
]
young = heapq.nsmallest(2,portfolio,key=lambda item:item['age'])
print(young)