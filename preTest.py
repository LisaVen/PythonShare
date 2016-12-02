# 1 Необходимо вывести значение A в системе счисления с основанием k без лидирующих нулей
# n, a, k = map(int, input().split())
# a = int(str(a),n)
# ret =[]
#
# if n>k:
#     while a>0:
#         ret.append(a%k)
#         a //= k
# elif n == k:
#     print(a)
# for i in ret[::-1]:
#     print(i, end="")

# 2 Определите количество пар чисел, первое из которых чётно, второе делится на 7, при этом хотя бы одно из них не менее чем трёхзначное
# x,y = map(int, input().split())
# counter = 0
# while(x!=0 and y !=0 ):
#     if x%2==0 and y%7==0 and (x>99 or y>99):
#         counter+=1
#     x,y = map(int, input().split())
# print(counter)

# 3 Определите, сколько элементов этой последовательности равны ее наибольшему элементу.
# max = 0
# samers = 1
# s = map( int, input().split())
# for i in s:
#     if i>max:
#         max = i
#         samers = 1
#     elif i == max:
#         samers+=1
# print(samers)

# 4 Найти количество видов одинаково популярных товаров, вторых по популярности.
# s = map(int, input().split())
# D = dict()
# for i in s:
#     if i in D:
#         D[i]+=1
#     else:
#         D[i]=1
#
# D2 = sorted(D.items(), key= lambda item: item[1])
# # print(D)
#
# counter = 0
# for key in D.keys():
#     if D[key] == D2[-2][1]:
#         counter +=1
#
# print(counter)

# 5 Синхронная сортировка массивов (БРЕД)

# 6 Дан массив списком чисел в одной строке. Посчитать, сколько перестановок будет
# совершено при сортировке этого массива сортировкой методом пузырька.
# x = list(map(int, input().split()))
# counter = 0
# for i in range(len(x)):
#     for j in range(i,len(x)-1):
#         if x[j]>x[j+1]:
#             x[j], x[j+1] = x[j+1], x[j]
#             counter+=1
#
# print(counter)
# print(x)

# 7 Ханойские башни. Ремонт в Ханое
# n = int(input())
#
# H = dict()
# H[1] = [x for x in range(n,0,-1)]
# H[2] = []
# H[3] = []
#
# def reput(i, k, n): # from, to, how many
#     if i+k!=5:
#         if n == 1:
#             disk = H[i].pop()
#             H[k].append(disk)
#             print("Move disk %d from %d to %d" %(disk,i,k))
#         else:
#             reput(i, 6-k-i, n-1)
#             reput(i,k,1)
#             reput(6-k-i,k,n-1)
#     else: # between 2 and 3
#         reput(i,1,n)
#         reput(1,k,n)
#
# reput(1, 3, n)

# 8 Требуется узнать, какая наименьшая сумма понадобится мальчику, чтобы добраться до верхней ступеньки.
# N = int(input())
# prices = list(map(int,input().split()))
#
# def cost(n=N):
#     if n < 0:
#         return 0
#     else:
#         minPred = min(cost(n-1),cost(n-2))
#         # print(minPred)
#         return minPred + prices[n-1]
#
# print(cost())

# 9 Ваша же задача состоит в нахождении количества способов разделить имеющиеся деньги между всеми
# участниками этих славных событий: K детьми лейтенанта Шмидта и Остапом Бендером.
#
# a = int(input())  #купюры
# b = int(input()) + 1 #дети и Остап
#
# def fac(n, pred=1):
#     if n<2:
#         return pred
#     else:
#         return fac(n-1, n*pred)
#
# print(int(fac(a + b - 1) / fac(a) / fac(b - 1)))

# 10
# class String():
#     def __init__(self, s=''):
#         self.__s = s
#
#     def print(self):
#         print(self.__s)
#
#     def check(self):
#         balance = 0
#         for c in self.__s:
#             if c=='(':
#                 balance+=1
#             elif c == ')':
#                 balance-=1
#             else:
#                 print(1==0)
#                 return
#             if balance<0:
#                 print(1==0)
#                 return
#         print(balance == 0)
#
#     def add(self,c):
#         self.__s+=c
#
# s = "((()))"
# ch = String(s)
# ch.check()
# ch.add('(')
# ch.check()
# ch.add(')')
# ch.check()
# ch.print()
