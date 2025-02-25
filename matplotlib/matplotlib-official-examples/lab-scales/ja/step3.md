# 対数スケールのプロットを作成する

次に調べるスケール変換のタイプは対数です。対数スケールのプロットを作成するには、`set_yscale()` メソッドを使用して文字列 `'log'` を渡します。また、プロットにタイトルとグリッドを追加します。

```python
# log
plt.plot(x, y)
plt.yscale('log')
plt.title('Logarithmic Scale')
plt.grid(True)
```
