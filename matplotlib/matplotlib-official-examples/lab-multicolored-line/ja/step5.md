# カラーバーの作成

色と `dydx` の値の間のマッピングを示すためにカラーバーを作成します。`matplotlib.pyplot` の `colorbar` 関数を使ってカラーバーを作成します。

```python
line = plt.gca().add_collection(lc)
plt.colorbar(line)
```
