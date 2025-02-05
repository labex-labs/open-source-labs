# 选择列

`usecols` 参数用于选择要导入哪些列。它接受一个整数或一个整数序列，这些整数对应于要导入的列的索引。

```python
np.genfromtxt(StringIO(data), usecols=(0, -1))
```
