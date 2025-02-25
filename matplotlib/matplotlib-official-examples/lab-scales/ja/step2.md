# 線形スケールのプロットを作成する

まず調べるスケール変換のタイプは線形です。これはMatplotlibで使用される既定のスケールです。線形スケールのプロットを作成するには、`set_yscale()` メソッドを使用して文字列 `'linear'` を渡します。また、プロットにタイトルとグリッドを追加します。

```python
# linear
plt.plot(x, y)
plt.yscale('linear')
plt.title('Linear Scale')
plt.grid(True)
```
