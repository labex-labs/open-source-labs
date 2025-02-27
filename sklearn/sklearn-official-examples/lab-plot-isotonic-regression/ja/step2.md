# データを生成する

次に、回帰に使用するデータを生成します。同分散な一様ノイズを持つ非線形な単調なトレンドを作成します。

```python
n = 100
x = np.arange(n)
rs = check_random_state(0)
y = rs.randint(-50, 50, size=(n,)) + 50.0 * np.log1p(np.arange(n))
```
