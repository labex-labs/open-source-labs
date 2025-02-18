# タイトルを上部に配置する

`subplots()` 関数と `set_xlabel()` 関数を使用して、タイトルを上部に配置したグラフを作成します。

```python
fig, ax = plt.subplots()
ax.plot(range(10))
ax.xaxis.set_label_position('top')
ax.set_xlabel('X-label')
ax.set_title('Top Title')
```
