Python 3.8.0 (v3.8.0:fa919fdf25, Oct 14 2019, 10:23:27) 
[Clang 6.0 (clang-600.0.57)] on darwin
Type "help", "copyright", "credits" or "license()" for more information.
>>> # Geo Distance
>>> x, y = eval(input('Enter Coordinat PintPoint as x & y:   '))
Enter Coordinat PintPoint as x & y:   29, 99
>>> Xd, Yd = eval(input('Enter Coordinate PintPoint as Xd, Yd: '))
Enter Coordinate PintPoint as Xd, Yd: 100, 77
>>> # compute it
>>> distance = ((x - Xd) * (x - Xd) + (y - Yd) * (y - Yd)) ** 0.5
>>> print('distance between them is:', distance)
distance between them is: 74.33034373659252
>>> 