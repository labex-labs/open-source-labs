# 対称的な対数スケールのプロットを作成する

調べる 3 番目のスケール変換のタイプは対称的な対数です。この種のスケールは、正と負の両方の値を含むデータを扱う際に便利です。対称的な対数スケールのプロットを作成するには、`set_yscale()` メソッドを使用して文字列 `'symlog'` を渡します。また、ゼロの周りの線形スケールにする値の範囲を指定するために、`linthresh` パラメータを `0.02` に設定します。また、プロットにタイトルとグリッドを追加します。

```python
# symmetric log
plt.plot(x, y - y.mean())
plt.yscale('symlog', linthresh=0.02)
plt.title('Symmetrical Logarithmic Scale')
plt.grid(True)
```
