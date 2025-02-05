# 模块

任何 Python 源文件都是一个模块。

```python
# foo.py
def grok(a):
 ...
def spam(b):
 ...
```

`import` 语句会加载并**执行**一个模块。

```python
# program.py
import foo

a = foo.grok(2)
b = foo.spam('Hello')
...
```
