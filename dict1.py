Python 3.14.3 (tags/v3.14.3:323c59a, Feb  3 2026, 16:04:56) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
#dict{}
a={"name":"mahesh","year":2003,"month":1}
print(a)
{'name': 'mahesh', 'year': 2003, 'month': 1}
type(a)
<class 'dict'>
b={"name","year","month"}
type(b)
<class 'set'>
a={"name":"mahesh","year":2003,"month":1}
a.keys()
dict_keys(['name', 'year', 'month'])
a.values()
dict_values(['mahesh', 2003, 1])
a.items()
dict_items([('name', 'mahesh'), ('year', 2003), ('month', 1)])
#accessing
a["year"]
2003
a[2026]
Traceback (most recent call last):
  File "<pyshell#12>", line 1, in <module>
    a[2026]
KeyError: 2026
a={"name":"mahesh","city":"vja"}
\
a.update({"mail id":"mahesh.vadladi201@gmail.com"})
a
{'name': 'mahesh', 'city': 'vja', 'mail id': 'mahesh.vadladi201@gmail.com'}
a.update({"date":20},{"month":1})
Traceback (most recent call last):
  File "<pyshell#16>", line 1, in <module>
    a.update({"date":20},{"month":1})
TypeError: update expected at most 1 argument, got 2
>>> a.update({"date":20,"month":1})
>>> a
{'name': 'mahesh', 'city': 'vja', 'mail id': 'mahesh.vadladi201@gmail.com', 'date': 20, 'month': 1}
>>> a={"time":6,"hour":5,"sec":10}
>>> a.setdefault("date",20)
20
>>> a
{'time': 6, 'hour': 5, 'sec': 10, 'date': 20}
>>> a={"colour":"black","food":"biriyani"}
>>> a.pop()
Traceback (most recent call last):
  File "<pyshell#23>", line 1, in <module>
    a.pop()
TypeError: pop expected at least 1 argument, got 0
>>> a.pop("colour")
'black'
>>> a
{'food': 'biriyani'}
>>> a.popitems()
Traceback (most recent call last):
  File "<pyshell#26>", line 1, in <module>
    a.popitems()
AttributeError: 'dict' object has no attribute 'popitems'. Did you mean: 'popitem'?
>>> a.pop(items)
Traceback (most recent call last):
  File "<pyshell#27>", line 1, in <module>
    a.pop(items)
NameError: name 'items' is not defined. Did you mean: 'iter'?
>>> a.pop(item)
Traceback (most recent call last):
  File "<pyshell#28>", line 1, in <module>
    a.pop(item)
NameError: name 'item' is not defined. Did you mean: 'iter'?
>>> a.popitem()
('food', 'biriyani')
>>> a
{}
