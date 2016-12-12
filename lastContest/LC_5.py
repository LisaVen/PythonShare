# def decompoza(n):
#     if n == 1:
#         return 1
#     elif n == 2:
#         return 2
#     else:
#         return
#
#
# n = int(input())
# print(decompoza(n))

n=int(input())
def decompoza(n):
    M=[1] + [0]*(n+1)
    for i in range(0,n):
        for j in range(i+1,n+1):
            M[j]+= M[j-i-1]
    print(M[n])
decompoza(n)