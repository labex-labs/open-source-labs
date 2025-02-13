# 对列表的每个元素执行函数

## 问题

编写一个函数 `for_each(itr, fn)`，它接受一个列表 `itr` 和一个函数 `fn` 作为参数。该函数应该对 `itr` 中的每个元素执行一次 `fn`。

## 示例

```python
def print_square(num):
    print(num*num)

for_each([1, 2, 3], print_square) # 输出 1 4 9
```

在上述示例中，`for_each` 函数使用列表 `[1, 2, 3]` 和函数 `print_square` 进行调用。`print_square` 函数对列表中的每个元素执行一次，打印出每个数字的平方。
