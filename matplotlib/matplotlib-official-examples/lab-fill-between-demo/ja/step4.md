# 軸全体にわたる水平領域の選択的なマーキング

同じ選択メカニズムを使用して、軸の垂直方向の全体の高さを塗りつぶすことができます。y 制限に依存しないように、データ座標で x 値を解釈し、軸座標で y 値を解釈する変換を追加します。次の例では、y データが指定されたしきい値を超えている領域をマークしています。

```python
fig, ax = plt.subplots()
x = np.arange(0, 4 * np.pi, 0.01)
y = np.sin(x)
ax.plot(x, y, color='black')

threshold = 0.75
ax.axhline(threshold, color='green', lw=2, alpha=0.7)
ax.fill_between(x, 0, 1, where=y > threshold,
                color='green', alpha=0.5, transform=ax.get_xaxis_transform())
```
