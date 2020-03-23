Python 3.8.0 (v3.8.0:fa919fdf25, Oct 14 2019, 10:23:27) 
[Clang 6.0 (clang-600.0.57)] on darwin
Type "help", "copyright", "credits" or "license()" for more information.
>>> import turtle # Import turtle module
>>> turtle.showturtle()
>>> turtle.write("Haha, ugly turtle.")
>>> turtle.forward(80)
>>> turtle.left(45)
>>> turtle.forward(100)
>>> turtle.color('pink')
>>> turtle.goto(0, 50)
>>> turtle.penup()
>>> turtle.goto(50, -50)
>>> turtle.pendown()
>>> turtle.circle(150)
>>> turtle.goto(0.0)
Traceback (most recent call last):
  File "<pyshell#12>", line 1, in <module>
    turtle.goto(0.0)
  File "<string>", line 8, in goto
  File "/Library/Frameworks/Python.framework/Versions/3.8/lib/python3.8/turtle.py", line 1774, in goto
    self._goto(Vec2D(*x))
TypeError: type object argument after * must be an iterable, not float
>>> turtle.penup()
>>> turtle.goto(0, 0)
>>> turtle.goto(0, -50)
>>> turtle.color('blue')
>>> turtle.circle()
Traceback (most recent call last):
  File "<pyshell#17>", line 1, in <module>
    turtle.circle()
TypeError: circle() missing 1 required positional argument: 'radius'
>>> turtle.circle(100)
>>> turtle.pendown()
>>> turtle.circle(100)
>>> turtle.penup()
>>> turtle.color('orange')
>>> turtle.forward(-20, 0)
Traceback (most recent call last):
  File "<pyshell#23>", line 1, in <module>
    turtle.forward(-20, 0)
TypeError: forward() takes 1 positional argument but 2 were given
>>> turtle.pendown()
>>> turtle.backward(20, 0)
Traceback (most recent call last):
  File "<pyshell#25>", line 1, in <module>
    turtle.backward(20, 0)
TypeError: backward() takes 1 positional argument but 2 were given
>>> turtle.forward(-20, 0)
Traceback (most recent call last):
  File "<pyshell#26>", line 1, in <module>
    turtle.forward(-20, 0)
TypeError: forward() takes 1 positional argument but 2 were given
>>> turtle.goto(-20, 0)
>>> turtle.circle(50)
>>> 
