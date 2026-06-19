import turtle

side = 4
t = turtle.Turtle()
wn = turtle.Screen()
t.speed(0)
j = 0
k = max(range(5))
print(k)

for i in range(4):
    t.forward(side)
    t.right(90)

while j < max(range(400)):
    j += 1
    side += 1
    t.up()
    t.forward(side/36)
    t.left(90)
    t.forward(side/27)
    t.right(92)
    t.down()
    for i in range(4):
        t.forward(side)
        t.right(90)

wn.exitonclick()