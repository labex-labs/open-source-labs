# 部分文字列を抽出する

正規表現を使用して部分文字列を抽出することができます。`extract` メソッドは、少なくとも 1 つのキャプチャ グループを持つ正規表現を受け付けます。

```python
# 各文字列から最初の数字を抽出する
s = pd.Series(["a1", "b2", "c3"], dtype="string")
s.str.extract(r"(\d)", expand=False)
```
