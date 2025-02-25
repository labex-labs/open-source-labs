# 辞書内の値のキーを見つける

与えられた値を持つ、与えられた辞書内の最初のキーを見つける関数`find_key(dict, val)`を書きます。

あなたの関数は以下のことを行う必要があります。

- 辞書`dict`と値`val`を入力として受け取ります。
- `dictionary.items()`と`next()`を使って、値が`val`に等しい最初のキーを返します。
- キーを出力として返します。

```python
def find_key(dict, val):
  return next(key for key, value in dict.items() if value == val)
```

```python
ages = {
  'Peter': 10,
  'Isabel': 11,
  'Anna': 9,
}
find_key(ages, 11) # 'Isabel'
```
