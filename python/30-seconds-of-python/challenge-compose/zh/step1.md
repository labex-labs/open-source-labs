# 组合函数

## 问题

编写一个名为 `compose(*fns)` 的函数，它接受一个或多个函数作为参数，并返回一个新函数，该新函数是从右到左组合输入函数的结果。最后一个（最右边的）函数可以接受一个或多个参数；其余函数必须是一元函数。

## 示例

```python
add5 = lambda x: x + 5
multiply = lambda x, y: x * y
multiply_and_add_5 = compose(add5, multiply)
multiply_and_add_5(5, 2) # 15
```

在上面的示例中，我们定义了两个函数 `add5` 和 `multiply`。然后，我们使用 `compose()` 函数创建一个名为 `multiply_and_add_5` 的新函数，该函数首先将其两个参数相乘，然后将 5 添加到结果中。当我们调用 `multiply_and_add_5(5, 2)` 时，我们得到结果 `15`。
