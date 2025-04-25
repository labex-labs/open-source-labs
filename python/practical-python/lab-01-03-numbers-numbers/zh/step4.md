# 浮点数（float）

使用十进制或指数记数法来指定浮点数：

```python
a = 37.45
b = 4e5 # 4 x 10**5 或 400,000
c = -1.345e-10
```

浮点数使用原生 CPU 表示法 [IEEE 754](https://en.wikipedia.org/wiki/IEEE_754) 以双精度表示。这与编程语言 C 中的 `double` 类型相同。

> 17 位精度\
> 指数范围从 -308 到 308

请注意，在表示小数时，浮点数是不精确的。

```python
>>> a = 2.1 + 4.2
>>> a == 6.3
False
>>> a
6.300000000000001
>>>
```

这 **不是 Python 的问题**，而是 CPU 底层的浮点硬件问题。

常见操作：

    x + y      加法
    x - y      减法
    x * y      乘法
    x / y      除法
    x // y     整除
    x % y      取模
    x ** y     幂运算
    abs(x)     绝对值

这些运算符与整数的运算符相同，除了按位运算符。更多数学函数可在 `math` 模块中找到。

```python
import math
a = math.sqrt(x)
b = math.sin(x)
c = math.cos(x)
d = math.tan(x)
e = math.log(x)
```
