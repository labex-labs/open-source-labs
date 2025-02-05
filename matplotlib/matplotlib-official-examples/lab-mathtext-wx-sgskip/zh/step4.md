# 定义函数

定义应用程序将显示的函数列表。每个函数由一个数学文本和一个 lambda 函数定义，该 lambda 函数接受一个输入值并返回一个输出值。

```python
functions = [
    (r'$\sin(2 \pi x)$', lambda x: np.sin(2*np.pi*x)),
    (r'$\frac{4}{3}\pi x^3$', lambda x: (4/3)*np.pi*x**3),
    (r'$\cos(2 \pi x)$', lambda x: np.cos(2*np.pi*x)),
    (r'$\log(x)$', lambda x: np.log(x))
]
```
