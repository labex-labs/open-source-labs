# 根据函数计算列表元素之和

## 问题

编写一个函数 `sum_by(lst, fn)`，它接受一个列表 `lst` 和一个函数 `fn` 作为参数。该函数应使用提供的函数将列表的每个元素映射到一个值，并返回这些值的总和。

## 示例

```python
sum_by([{ 'n': 4 }, { 'n': 2 }, { 'n': 8 }, { 'n': 6 }], lambda v : v['n']) # 20
```

在上述示例中，`sum_by()` 函数接受一个字典列表和一个 lambda 函数，该函数从每个字典中提取 `'n'` 键的值。该函数将每个字典映射到其 `'n'` 值，并返回这些值的总和，即 `20`。
