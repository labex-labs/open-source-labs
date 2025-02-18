# プロットのカスタマイズ

基本的なプロットができたので、これをカスタマイズしてみましょう。

```python
x = [1, 2, 3, 4, 5]
y = [2, 4, 6, 8, 10]

plt.plot(x, y, color='red', marker='o')
plt.title('My Plot')
plt.xlabel('X Axis Label')
plt.ylabel('Y Axis Label')
plt.show()
```

ここでは、プロットにいくつかのカスタマイズを加えています。線の色を赤色に変更し、各データポイントに円形のマーカーを追加しています。また、プロットにタイトルと軸ラベルも追加しています。
