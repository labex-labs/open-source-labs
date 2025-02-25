# 変換の微調整

`converters` 引数を使うと、より複雑な変換を処理するための変換関数を定義できます。列インデックスまたは列名をキーとし、変換関数を値とする辞書を受け付けます。

```python
convertfunc = lambda x: float(x.strip(b"%"))/100.
np.genfromtxt(StringIO(data), converters={1: convertfunc})
```
