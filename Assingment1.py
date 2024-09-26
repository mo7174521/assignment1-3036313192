from turtle import *

def draw_soviet_flag():
# 设置画布和速度
setup(800, 600)
speed(10)

# 绘制红色背景
bgcolor("red")
penup()
goto(-400, 300)
pendown()
begin_fill()
for _ in range(2):
forward(800)
right(90)
forward(600)
right(90)
end_fill()

# 绘制镰刀
penup()
goto(-100, 50)
setheading(0)
pendown()
pensize(5)
fillcolor("gold")
begin_fill()
# 锯齿部分
left(45)
forward(50)
right(90)
forward(20)
left(90)
forward(50)
end_fill()

# 锤子
penup()
goto(-50, 50)
pendown()
fillcolor("gold")
begin_fill()
setheading(0)
forward(20)
right(90)
forward(60)
right(90)
forward(20)
right(90)
forward(60)
end_fill()

# 绘制镰刀的手柄
penup()
goto(-100, -50)
setheading(0)
pendown()
fillcolor("gold")
begin_fill()
setheading(-90)
forward(10)
right(90)
forward(30)
right(90)
forward(10)
right(90)
forward(30)
end_fill()

# 完成绘制
penup()
goto(0, 0)
done()

draw_soviet_flag()


