Python 3.14.3 (tags/v3.14.3:323c59a, Feb  3 2026, 16:04:56) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
#sets{}
a={3,5.7,"mahesh",5+9j,True,False}
print(a)
{False, True, (5+9j), 3, 5.7, 'mahesh'}
type(a)
<class 'set'>
b={7,9,5,6,7,9,3}
b
{3, 5, 6, 7, 9}
type(b)
<class 'set'>
a={4,5,6,7,8,9}
a.add(20)
a
{4, 5, 6, 7, 8, 9, 20}
#issubset()
a={2,3,4,5,6,7}
b={5,6,7}
b.issubset(a)
True
a.issubset(b)
False
a={4,5,6,7,8,9}
b={8,9,10,11}
b.issubset(a)
False
a.issubset(b)
False
a={3,4,5,6,7,8,9}
b={2,3,4,5,6}
a.issuperset(b)
False
a={1,2,3,4,5,6}
b={4,5,6}
a.issuperset(b)
True
b.issubset(a)
True
#union()
a={3,4,5,6,7,8}
b={2,3,4,5,9}
a.union(b)
{2, 3, 4, 5, 6, 7, 8, 9}
#intersection
a={4,5,6,7,8,9}
b={6,7,8,9,10,11}
a.intersection(b)
{8, 9, 6, 7}
a={2,3,4,5,6}
b={3,4,5,6,7,8}
a.difference(b)
{2}
b.difference(a)
{8, 7}
a={10,11,12,13,14}
b={11,12,13,14,15}
a.update(b)
a
{10, 11, 12, 13, 14, 15}
b
{11, 12, 13, 14, 15}
b.update(a)
b
{10, 11, 12, 13, 14, 15}
a={4,5,6,7,8,9}
b={2,3,4,5,6,7,8,9,10}
a.difference_update(b)
a
set()
b.difference_update(a)
b
{2, 3, 4, 5, 6, 7, 8, 9, 10}
a={2,3,4,5,6,7}
b={1,5,7,9,11,12}
a.difference_update(b)
a
{2, 3, 4, 6}
b.difference_update(a)
b
{1, 5, 7, 9, 11, 12}
a={3,4,5,6,7,8,9}
b={1,2,3,8,9,10,11}
a.symmetric_difference(b)
{1, 2, 4, 5, 6, 7, 10, 11}
b.symmetric_difference(a)
{1, 2, 4, 5, 6, 7, 10, 11}
a={1,3,5,7,9,11,13}
b={2,3,4,6,8,10,12}
a.symmetric_difference_update(b)
a
{1, 2, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13}
b.symmetric_difference_update(a)
b
{1, 3, 5, 7, 9, 11, 13}
a={7,8,9,10,11,12,13}
b={2,3,4,5,6,7,8,9}
a.intersection_update(b)
a
{8, 9, 7}
b.intersection(a)
{8, 9, 7}
b.intersection_update(a)
a
{8, 9, 7}
b
{8, 9, 7}
a={5,6,7,8,9,10}
a.pop()
5
a.pop(4)
Traceback (most recent call last):
  File "<pyshell#77>", line 1, in <module>
    a.pop(4)
TypeError: set.pop() takes no arguments (1 given)
a.remove(10)
>>> a
{6, 7, 8, 9}
>>> a={3,4,5,6,7}
>>> a.copy()
{3, 4, 5, 6, 7}
>>> a.clear()
>>> a
set()
>>> b
{8, 9, 7}
>>> b.discard()
Traceback (most recent call last):
  File "<pyshell#85>", line 1, in <module>
    b.discard()
TypeError: set.discard() takes exactly one argument (0 given)
>>> b.discard(9)
>>> b
{8, 7}
>>> a={3,4,5,6,7,8}
>>> b={2,4,5,6,7}
>>> a.isdisjoint(b)
False
>>> a={6,7,8}
>>> b={1,2,3}
>>> a.isdisjoint(b)
True
>>> a={5,7,8,9}
>>> len(a)
4
>>> a.count(5)
Traceback (most recent call last):
  File "<pyshell#96>", line 1, in <module>
    a.count(5)
AttributeError: 'set' object has no attribute 'count'
>>> a.index(4)
Traceback (most recent call last):
  File "<pyshell#97>", line 1, in <module>
    a.index(4)
AttributeError: 'set' object has no attribute 'index'
