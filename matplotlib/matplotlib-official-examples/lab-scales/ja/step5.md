# ロジットスケールのプロットを作成する

調べる4番目のスケール変換のタイプはロジットです。この種のスケールは、0と1で境界付けられたデータを扱う際に便利です。ロジットスケールのプロットを作成するには、`set_yscale()` メソッドを使用して文字列 `'logit'` を渡します。また、プロットにタイトルとグリッドを追加します。

```python
# logit
plt.plot(x, y)
plt.yscale('logit')
plt.title('Logit Scale')
plt.grid(True)
```
