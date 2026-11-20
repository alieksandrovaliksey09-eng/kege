from turtle import *
tracer(0)
screensize(2000, 2000)
lt(90)
m = 20

for i in range(4):
    fd(12 * m)
    lt(90)

up()
rt(270)
bk(-7 * m)
lt(180)
down()

for i in range(4):
    fd(8 * m)
    rt(270)

up()
for x in range(-20, 20):
    for y in range(-20, 20):
        goto(x * m, y * m)
        dot(3, 'red')

print(8 * 2 + 9 * 2)

update()
