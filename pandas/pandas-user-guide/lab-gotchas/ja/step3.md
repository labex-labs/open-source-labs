# ユーザー定義関数 (UDF) メソッドによる変更

UDF を受け取る pandas メソッドを使用する場合、UDF 内で DataFrame を変更しないようにしましょう。代わりに、変更を加える前にコピーを作成します。

```python
def f(s):
    s = s.copy()
    s.pop("a")
    return s

df = pd.DataFrame({"a": [1, 2, 3], 'b': [4, 5, 6]})
df.apply(f, axis="columns")
```
