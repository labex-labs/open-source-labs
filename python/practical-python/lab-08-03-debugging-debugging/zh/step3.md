# 使用交互式解释器（REPL）

使用选项`-i`在执行脚本时保持Python处于活动状态。

```bash
$ python3 -i blah.py
Traceback (most recent call last):
  File "blah.py", line 13, in?
    foo()
  File "blah.py", line 10, in foo
    bar()
  File "blah.py", line 7, in bar
    spam()
  File "blah.py", 4, in spam
    line x.append(3)
AttributeError: 'int' object has no attribute 'append'
>>>
```

它会保留解释器的状态。这意味着在程序崩溃后你可以四处查看。检查变量值和其他状态。
