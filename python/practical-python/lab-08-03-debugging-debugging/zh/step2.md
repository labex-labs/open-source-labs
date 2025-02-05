# 解读回溯信息

最后一行是崩溃的具体原因。

```bash
$ python3 blah.py
Traceback (most recent call last):
  File "blah.py", line 13, in?
    foo()
  File "blah.py", line 10, in foo
    bar()
  File "blah.py", line 7, in bar
    spam()
  File "blah.py", 4, in spam
    line x.append(3)
# 崩溃原因
AttributeError: 'int' object has no attribute 'append'
```

然而，它并不总是易于阅读或理解。

专业提示：将整个回溯信息粘贴到谷歌中。
