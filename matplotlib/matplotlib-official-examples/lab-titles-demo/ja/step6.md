# Y 軸位置を手動で設定する

`title()` 関数の `y` パラメータを使用して、タイトルの垂直位置を手動で指定します。

```python
fig, ax = plt.subplots()
ax.plot(range(10))
ax.xaxis.set_label_position('top')
ax.set_xlabel('X-label')
ax.set_title('Manual Y Positioning', y=1.0)
```
