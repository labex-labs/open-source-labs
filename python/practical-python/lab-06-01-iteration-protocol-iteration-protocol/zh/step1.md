# 随处可见的迭代

许多不同的对象都支持迭代。

```python
a = 'hello'
for c in a: # 遍历字符串a中的字符
  ...

b = { 'name': 'Dave', 'password':'foo'}
for k in b: # 遍历字典中的键
  ...

c = [1,2,3,4]
for i in c: # 遍历列表/元组中的元素
  ...

f = open('foo.txt')
for x in f: # 遍历文件中的行
  ...
```
