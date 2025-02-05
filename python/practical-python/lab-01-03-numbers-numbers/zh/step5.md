# 比较运算

以下比较 / 关系运算符可用于数字：

    x < y      小于
    x <= y     小于或等于
    x > y      大于
    x >= y     大于或等于
    x == y     等于
    x!= y     不等于

你可以使用 `and`（与）、`or`（或）、`not`（非）来构成更复杂的布尔表达式。

以下是一些示例：

```python
if b >= a and b <= c:
    print('b 在 a 和 c 之间')

if not (b < a or b > c):
    print('b 仍然在 a 和 c 之间')
```
