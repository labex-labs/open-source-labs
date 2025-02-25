# 単純なピッキング、線、矩形、およびテキスト

アーティストの「picker」プロパティを設定することで単純なピッキングを有効にします。これにより、マウスイベントがアーティストの上にある場合、アーティストがピックイベントを発生させることができるようになります。線、矩形、およびテキストを含む単純なプロットを作成し、これらの各アーティストにピッキングを有効にします。

```python
fig, (ax1, ax2) = plt.subplots(2, 1)
ax1.set_title('click on points, rectangles or text', picker=True)
ax1.set_ylabel('ylabel', picker=True, bbox=dict(facecolor='red'))
line, = ax1.plot(rand(100), 'o', picker=True, pickradius=5)

# Pick the rectangle.
ax2.bar(range(10), rand(10), picker=True)
for label in ax2.get_xticklabels():  # Make the xtick labels pickable.
    label.set_picker(True)
```
