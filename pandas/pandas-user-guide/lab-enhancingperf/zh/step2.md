# 实现纯 Python 函数

我们将首先创建一个纯 Python 函数，该函数按行对 DataFrame 进行操作。

```python
# 定义一个函数
def f(x):
    return x * (x - 1)

# 定义另一个使用第一个函数的函数
def integrate_f(a, b, N):
       s = 0
       dx = (b - a) / N
       for i in range(N):
           s += f(a + i * dx)
       return s * dx
```
