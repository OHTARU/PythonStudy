# # 7 - 1 - 1
# from datetime import date

# start_date = date(2019, 2, 24)
# today = date.today()

# elapsed_days = (today - start_date).days

# print("춘향이와 몽룡이의 연애 시작일 : {}년 {}월 {}일".format(start_date.year, start_date.month, start_date.day))
# print("연애 시작일로부터 경과한 날짜 : {}일".format(elapsed_days))


# # 7 - 1 - 2
# from datetime import date, timedelta

# start_date = date(2019, 2, 24)

# days = [100, 200, 500, 1000]
# for d in days:
#     anniversary = start_date + timedelta(days=d)
#     print("춘향이와 몽룡이의 {}일 기념일 : {}년 {}월 {}일".format(d, anniversary.year, anniversary.month, anniversary.day))

# # 7 - 2 - 1
# import time

# def sum1to1000000():
#     return sum(range(1, 1000001))

# start_time = time.time()
# sum1to1000000()
# elapsed_time = time.time() - start_time

# print("함수 실행 시간 : {}초".format(elapsed_time))


# # 7 - 2 - 2
# start_time = time.time()

# for _ in range(100):
#     sum1to1000000()

# elapsed_time = time.time() - start_time

# print("100번 호출에 소요된 시간 : {}초".format(elapsed_time))

# # 7 - 3 - 1
# import time
# import math
# def print_hello():
#     print("Hello Python!")

# # 7 - 3 - 2
# def factorial_1000():
#     return math.factorial(1000)

# # 7 - 3 - 3
# def sum_of_cubes():
#     return sum(i**3 for i in range(1, 1001) if i % 2 != 0)

# # 7 - 3 - 4
# def sum_of_sins():
#     return sum(math.sin(math.radians(i)) for i in range(1, 361))

# functions = [print_hello, factorial_1000, sum_of_cubes, sum_of_sins]

# for func in functions:
#     start_time = time.time()

#     for _ in range(100):
#         func()

#     elapsed_time = time.time() - start_time

#     print("{} 함수를 100번 호출하는데 걸린 시간 : {}초".format(func.__name__, elapsed_time))


# # 7 - 4 - 2
# import time

# def my_rand():
#     a = 1103515245
#     c = 12345
#     m = 2**31
#     seed = int(time.time())
#     for _ in range(10):
#         seed = (a*seed + c) % m
#         yield seed % 1000001

# for rand_num in my_rand():
#     print(rand_num)

# # 7 - 5
# import math


# def degrees_to_radians(degrees):
#     return degrees * math.pi / 180


# for degrees in range(0, 181, 10):
#     radians = degrees_to_radians(degrees)
#     print("sin({}) = {:.3f}, cos({}) = {:.3f}, tan({}) = {:.3f}".format(
#         degrees, math.sin(radians), 
#         degrees, math.cos(radians), 
#         degrees, math.tan(radians) ))


# # 7 - 6

# import math

# for i in range(11):
#     print("sqrt({}) = {:.3f}".format(i, math.sqrt(i)))


# # 7 - 7 - 1
# import math

# log_values = {}
# for i in range(1, 301, 30):
#     log_values[i] = round(math.log(i), 3)

# print("결과값: ", log_values)

# # 7 - 7 - 2
import turtle
import math

window = turtle.Screen()
window.bgcolor("white")
log_turtle = turtle.Turtle()
log_turtle.color("red")

log_turtle.penup()
log_turtle.goto(-200, 0)
log_turtle.pendown()
log_turtle.forward(400)
log_turtle.penup()
log_turtle.goto(0, -200)
log_turtle.pendown()
log_turtle.left(90)
log_turtle.forward(400)
log_turtle.penup()
log_turtle.goto(0, 0)
log_turtle.pendown()
for x in range(0, 361, 5):
    y = round(math.log(x+1), 3) * 50
    log_turtle.goto(x-180, y)

window.onclick(lambda x, y: window.bye())


turtle.done()


# # 7 - 7 - 3

# log_turtle.penup()
# log_turtle.goto(0, 0)
# log_turtle.pendown()
# for x in range(0, 361, 5):
#     y = round(math.log(x+1), 3) * 500  # y = log(x), 스케일을 위해 * 500
#     log_turtle.goto(x-180, y)


# # 7 - 7 - 4

# sin_turtle = turtle.Turtle()
# sin_turtle.color("red")
# sin_turtle.penup()
# sin_turtle.goto(-360, 0)
# sin_turtle.pendown()
# for x in range(-360, 361):
#     y = math.sin(math.radians(x)) * 100  
#     sin_turtle.goto(x, y)


# cos_turtle = turtle.Turtle()
# cos_turtle.color("blue")
# cos_turtle.penup()
# cos_turtle.goto(-360, 0)
# cos_turtle.pendown()
# for x in range(-360, 361):
#     y = math.cos(math.radians(x)) * 100  
#     cos_turtle.goto(x, y)


# # 7 - 8
# import random

# romeo_dice = random.randrange(1, 7)
# juliet_dice = random.randrange(1, 7)

# print("로미오의 주사위 숫자는 {} 입니다.".format(romeo_dice))
# print("줄리엣의 주사위 숫자는 {} 입니다.".format(juliet_dice))

# if romeo_dice > juliet_dice:
#     print("로미오가 이겼습니다.")
# elif juliet_dice > romeo_dice:
#     print("줄리엣이 이겼습니다.")
# else:
#     print("비겼습니다.")

# # 7 - 9
# import random

# rps = ['가위', '바위', '보']

# romeo_choice = random.choice(rps)
# juliet_choice = random.choice(rps)

# print("로미오의 선택은 {} 입니다.".format(romeo_choice))
# print("줄리엣의 선택은 {} 입니다.".format(juliet_choice))

# if romeo_choice == juliet_choice:
#     print("비겼습니다.")
# elif (romeo_choice == '가위' and juliet_choice == '보') or (romeo_choice == '바위' and juliet_choice == '가위') or (romeo_choice == '보' and juliet_choice == '바위'):
#     print("로미오가 이겼습니다.")
# else:
#     print("줄리엣이 이겼습니다.")


# # 7 - 10
# import random


# x = random.randint(1, 20)


# n = 0

# while True:
#     user_input = int(input("1~20 사이의 숫자를 입력해주세요: "))
#     n += 1 


#     if user_input < x:
#         print("{}보다 작습니다.".format(user_input))
#     elif user_input > x:
#         print("{}보다 큽니다.".format(user_input))
#     else:
#         print("정답입니다!")
#         if n <= 3:
#             print("{}번 만에 맞춘 당신은 천재!".format(n))
#         elif 3 < n <= 6:
#             print("{}번 만에 맞추셨네요. 잘 했어요^^".format(n))
#         else:
#             print("{}번 만에 맞추다니 쩝쩝...".format(n))
#         break


# # 7 - 11
# import turtle

# side_length = 100

# t = turtle.Turtle()

# for _ in range(5):
#     t.forward(side_length)
#     t.right(360 / 5)

# t.penup()
# t.goto(200, 0)
# t.pendown()

# for _ in range(6):
#     t.forward(side_length)
#     t.right(360 / 6)

# t.penup()
# t.goto(400, 0)
# t.pendown()

# for _ in range(8):
#     t.forward(side_length)
#     t.right(360 / 8)

# turtle.done()


# # 7 - 12
# import turtle

# t = turtle.Turtle()
# radius = 50


# olympic_positions = [(-200, 0), (-100, 0), (0, 0), (-150, -50), (-50, -50)]
# for position in olympic_positions:
#     t.penup()
#     t.goto(position)
#     t.pendown()
#     t.circle(radius)

# t.penup()
# t.goto(300, 0)
# t.pendown()

# audi_positions = [(300, 0), (350, 0), (400, 0), (450, 0)]
# for position in audi_positions:
#     t.penup()
#     t.goto(position)
#     t.pendown()
#     t.circle(radius)

# turtle.done()
