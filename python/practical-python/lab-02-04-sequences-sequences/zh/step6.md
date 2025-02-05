# break 语句

你可以使用 `break` 语句提前退出循环。

```python
for name in namelist:
    if name == 'Jake':
        break
  ...
  ...
statements
```

当 `break` 语句执行时，它会退出循环并继续执行下一个 `statements`。`break` 语句仅适用于最内层的循环。如果这个循环在另一个循环内部，它不会中断外层循环。
