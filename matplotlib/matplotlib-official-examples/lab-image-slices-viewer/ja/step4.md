# プロットを作成してスクロールイベントを接続する

Matplotlib の `subplots` 関数を使ってプロットを作成し、作成した `IndexTracker` オブジェクトを渡します。その後、`mpl_connect` を使ってスクロールイベントをグラフキャンバスに接続します。

```python
fig, ax = plt.subplots()
tracker = IndexTracker(ax, X)

fig.canvas.mpl_connect('scroll_event', tracker.on_scroll)
plt.show()
```
