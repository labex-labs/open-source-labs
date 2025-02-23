# アニメーション関数の作成

新しいランダムなデータを生成し、長方形の高さを更新する `animate` 関数を作成する必要があります。

```python
def animate(frame_number):
    # simulate new data coming in
    data = np.random.randn(1000)
    n, _ = np.histogram(data, HIST_BINS)
    for count, rect in zip(n, bar_container.patches):
        rect.set_height(count)
    return bar_container.patches
```
