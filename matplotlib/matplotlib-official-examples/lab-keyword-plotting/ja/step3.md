# データを作成する

このステップでは、変数 `a`、`b`、`c`、および `d` の値を含む辞書 `data` を作成します。

```python
data = {'a': np.arange(50),
        'c': np.random.randint(0, 50, 50),
        'd': np.random.randn(50)}

data['b'] = data['a'] + 10 * np.random.randn(50)
data['d'] = np.abs(data['d']) * 100
```
