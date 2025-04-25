# 水平領域の選択的な塗りつぶし

パラメータの*where*を使用すると、塗りつぶす x 範囲を指定できます。これは、*x*と同じサイズのブール配列です。連続した*True*シーケンスの x 範囲のみが塗りつぶされます。したがって、隣接する*True*と*False*の値の間の範囲は決して塗りつぶされません。したがって、データポイントの x 距離が十分に小さく、上記の効果が目立たない場合を除き、`interpolate=True`を設定することをお勧めします。

```python
x = np.array([0, 1, 2, 3])
y1 = np.array([0.8, 0.8, 0.2, 0.2])
y2 = np.array([0, 0, 1, 1])

fig, (ax1, ax2) = plt.subplots(2, 1, sharex=True)

ax1.set_title('interpolation=False')
ax1.plot(x, y1, 'o--')
ax1.plot(x, y2, 'o--')
ax1.fill_between(x, y1, y2, where=(y1 > y2), color='C0', alpha=0.3)
ax1.fill_between(x, y1, y2, where=(y1 < y2), color='C1', alpha=0.3)

ax2.set_title('interpolation=True')
ax2.plot(x, y1, 'o--')
ax2.plot(x, y2, 'o--')
ax2.fill_between(x, y1, y2, where=(y1 > y2), color='C0', alpha=0.3,
                 interpolate=True)
ax2.fill_between(x, y1, y2, where=(y1 <= y2), color='C1', alpha=0.3,
                 interpolate=True)
fig.tight_layout()
```
