import turtle as t

# # 1. Фибоначи
# # 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377, 610 …
# def nextF(n):
#     if n < 3:
#         return 1
#     else:
#         return nextF(n-1) + nextF(n-2)
#
# print(nextF(13))

# # 2. Снежинка Коха
# def line(L, n):
#     if n == 1:
#         t.forward(L)
#     else:
#         line(L/3, n-1)
#         t.left(60)
#         line(L/3,n-1)
#         t.right(120)
#         line(L/3,n-1)
#         t.left(60)
#         line(L/3,n-1)
#
# def initT():
#     t.shape("circle")
#     t.speed(0)
#     t.penup()
#     t.goto(-240,+120)
#     t.pendown()
#
# def draw(L, N):
#     line(L,N)
#     t.right(120)
#     line(L,N)
#     t.right(120)
#     line(L,N)
#     t.done()
#
# initT()
# N = 5
# L = 486
# draw(L, N)


# # 4. Кривая Минковского
# def initT():
#     # t.shape("circle")
#     t.speed(6)
#     t.penup()
#     t.goto(-260,0)
#     t.pendown()
#
# def line(L, n):
#     if n < 2:
#         t.forward(L)
#     else:
#         line(L/4, n-1)
#         t.left(90)
#         line(L/4,n-1)
#         t.right(90)
#         line(L/4,n-1)
#         t.right(90)
#         line(L/4,n-1)
#         line(L/4,n-1)
#         t.left(90)
#         line(L/4,n-1)
#         t.left(90)
#         line(L/4,n-1)
#         t.right(90)
#         line(L/4,n-1)
#
# def draw(L, N):
#     line(L, N)
#     t.done()
#
# initT()
# N = 4
# L = 500
# draw(L, N)

# # 5. Кривая Леви
# q = 2**0.5 # const
#
# def initT():
#     t.shape("circle")
#     t.speed(8)
#     t.penup()
#     t.goto(-150,-50)
#     t.pendown()
#
# def line(L, n):
#     if n == 1:
#         t.forward(L)
#     else:
#         t.left(45)
#         line(L/q, n-1)
#         t.right(90)
#         line(L/q, n-1)
#         t.left(45)
#
# def draw(L, N):
#     line(L, N)
#     t.done()
#
# initT()
# N = 10
# L = 300
# draw(L, N)

# 6. Кривая дракона
def initT():
    t.shape("circle")
    t.speed(0)
    t.penup()
    t.goto(-100,-200)
    t.pendown()
    t.right(90)

def createCode(n, code = ["1"]):
    if n == 1:
        return code
    else:
        code.append("1")
        code += invers(code[0:-1])
        return createCode(n-1, code)

def invers(s):
    ret = []
    for c in s:
        if c == '0':
            ret.append("1")
        else:
            ret.append("0")
    return ret[::-1]

def make1(l):
    t.left(90)
    t.forward(l)

def make0(l):
    t.right(90)
    t.forward(l)

def draw(L, N):
    code = createCode(N)
    for c in code:
        if c == "0":
            make0(L)
        else:
            make1(L)
    t.done()

initT()
N = 12
L = 90/N
draw(L, N)