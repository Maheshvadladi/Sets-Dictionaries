Python 3.14.3 (tags/v3.14.3:323c59a, Feb  3 2026, 16:04:56) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
a={"name":"mahesh","city":"vja","mail":"mahesh.vadladi@gmail.com"}
a.get("name")
'mahesh'
a.copy()
{'name': 'mahesh', 'city': 'vja', 'mail': 'mahesh.vadladi@gmail.com'}
>>> a.clear()
>>> a
{}
>>> b={}
>>> b.update({"moblie no":9347673497})
>>> b
{'moblie no': 9347673497}
>>> len(b)
1
>>> a={"year":2026,"month":2,"date":21}
>>> a.index("year")
Traceback (most recent call last):
  File "<pyshell#10>", line 1, in <module>
    a.index("year")
AttributeError: 'dict' object has no attribute 'index'
>>> a.count()
Traceback (most recent call last):
  File "<pyshell#11>", line 1, in <module>
    a.count()
AttributeError: 'dict' object has no attribute 'count'
>>> a={"name":"mahesh","year":2026,"name":"mahesh"}
>>> a
{'name': 'mahesh', 'year': 2026}
>>> a={"name":"mahesh","year":2026,"name":"manoj"}
>>> a
{'name': 'manoj', 'year': 2026}
>>> a={"name":"mahesh","year":2026,"name1":"mahesh"}
>>> a
{'name': 'mahesh', 'year': 2026, 'name1': 'mahesh'}
>>> a={"id_no":[10,20,30],"names":["mahesh","manoj"],"places":["vja","hyd","vzg"]}
>>> a
{'id_no': [10, 20, 30], 'names': ['mahesh', 'manoj'], 'places': ['vja', 'hyd', 'vzg']}
>>> a.keys()
dict_keys(['id_no', 'names', 'places'])
>>> a.values()
dict_values([[10, 20, 30], ['mahesh', 'manoj'], ['vja', 'hyd', 'vzg']])
>>> a.items()
dict_items([('id_no', [10, 20, 30]), ('names', ['mahesh', 'manoj']), ('places', ['vja', 'hyd', 'vzg'])])
