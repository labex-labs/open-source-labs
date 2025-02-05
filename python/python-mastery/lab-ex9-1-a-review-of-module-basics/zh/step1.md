# 准备工作

本练习涉及库模块中一些较为棘手的细节。通过创建一个非常简单的库模块来开始本练习：

```python
# simplemod.py

x = 42        # 一个全局变量

# 一个简单的函数
def foo():
    print('x is', x)

# 一个简单的类
class Spam:
    def yow(self):
        print('Yow!')

# 一个脚本语句
print('Loaded simplemod')
```
