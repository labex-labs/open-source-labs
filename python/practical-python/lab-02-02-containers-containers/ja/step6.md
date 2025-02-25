# 辞書の検索

キーの存在をテストできます。

```python
if key in d:
    # はい
else:
    # いいえ
```

存在しない可能性のある値を検索し、存在しない場合にデフォルト値を提供できます。

```python
name = d.get(key, default)
```

例：

```python
>>> prices.get('IBM', 0.0)
93.37
>>> prices.get('SCOX', 0.0)
0.0
>>>
```
