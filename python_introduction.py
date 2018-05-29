# print('hello')
# a = 1
# print(a)
# b = 2
# print(a + b)
# a = 2
# b = 3
# a > b # False
# a == 2 # True
# if b > a:
#     print('B is big')
# else:
#     print('B is small')
# a = True
# b = False
# if not b:
#     print('WOW')
# a = [10, 12, 8, 3]
# for i in a:
#     print(i)
# print(a[1]) # what will be printed?
# min(a), max(a), sum(a), len(a)
# a.append(21)
# lists are mutable:
# a[3] = 88
# print(a) # what will be printed?
# import random
# random.shuffle(a) #result: for example: [8, 10, 3, 12]
# b = random.choice(a) # result: for example 10
# c = random.sample(a, 2) # result: for example [3, 12]
# a = [8, 12, 7, 10]
# b = list(range(10))
# print(b)
# for i in a:
#     print(i**2)
# import random
# a = random.random()
# print(a)
# for i in b:
#     print(random.random())
# a = random.randint(0,100)
# print(a)
# a = [4, 3, 5, 15, 22, 28, 7]
# b = []
# for i in a:
#     if i < 15:
#     if i % 2 == 1:
#         b.append(i);
# print(b)
# import random
# c = [random.random() for i in range(10)]
# squares = [i**2 for i in range(5)]
# print(c)
# a = {'name': 'Philipp', 'surname': 'chappy', 'height': 179, 'nationality': 'Russian'}
# for i, v in a.items():
#     print(i,': ', v)
# price_per_square = 100
# garden_price = 1000
# def house_price(length,width):
#     space = length * width
#     return space * price_per_square
# def elite_house_price(length,width):
#     space = length * width
#     return space * price_per_square + garden_price
# my_house_price = house_price(10,20)
# trump_house_price = elite_house_price(100,200)
# def house_price(length,width,elite=False):
#     space = length * width
#     if elite:
#         return space = price_per_square + garden_price
#     return space * price_per_square