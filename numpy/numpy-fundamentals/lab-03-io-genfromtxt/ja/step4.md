# 列の選択

`usecols` 引数は、インポートする列を選択するために使用されます。インポートする列のインデックスに対応する単一の整数または整数のシーケンスを受け付けます。

```python
np.genfromtxt(StringIO(data), usecols=(0, -1))
```
