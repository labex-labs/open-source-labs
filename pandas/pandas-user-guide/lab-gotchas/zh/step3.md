# 使用用户定义函数 (UDF) 方法进行变异操作

在使用接受 UDF 的 pandas 方法时，避免在 UDF 内部修改 DataFrame。相反，在进行更改之前先进行复制。

```python
def f(s):
    s = s.copy()
    s.pop("a")
    return s

df = pd.DataFrame({"a": [1, 2, 3], 'b': [4, 5, 6]})
df.apply(f, axis="columns")
```
