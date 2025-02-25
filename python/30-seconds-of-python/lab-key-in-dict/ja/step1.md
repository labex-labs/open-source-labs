# 辞書にキーが存在するかどうかを確認する

辞書 `d` とキー `key` を引数として受け取り、辞書にキーが存在する場合は `True`、そうでない場合は `False` を返す関数 `key_in_dict(d, key)` を書きなさい。

```python
def key_in_dict(d, key):
  return (key in d)
```

```python
d = {'one': 1, 'three': 3, 'five': 5, 'two': 2, 'four': 4}
key_in_dict(d, 'three') # True
```
