# 测试列表中的每个元素是否为真值

## 问题

编写一个名为 `every(lst, fn = lambda x: x)` 的函数，该函数接受一个列表 `lst` 和一个函数 `fn` 作为参数。如果 `fn` 对列表中的每个元素都返回 `True`，则该函数应返回 `True`；否则返回 `False`。如果未提供函数，则该函数应默认使用恒等函数（`lambda x: x`）。

要解决此问题，你需要结合使用 `all()` 函数、`map()` 和提供的函数 `fn`，以检查 `fn` 对列表中的所有元素是否都返回 `True`。

## 示例

```python
every([4, 2, 3], lambda x: x > 1) # True
every([1, 2, 3]) # True
every([0, 1, 2]) # False
```
