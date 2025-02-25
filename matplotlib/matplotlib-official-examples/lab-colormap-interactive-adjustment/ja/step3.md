# グラフを作成する

データを生成したので、`imshow()` 関数を使ってグラフを作成します。

```python
fig, ax = plt.subplots()
im = ax.imshow(data2d)
ax.set_title('Pan on the colorbar to shift the color mapping\n'
             'Zoom on the colorbar to scale the color mapping')
```
