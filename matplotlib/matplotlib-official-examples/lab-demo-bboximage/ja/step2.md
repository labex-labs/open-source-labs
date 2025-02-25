# テキスト付きの BboxImage を作成する

まずは、テキスト付きの BboxImage を作成します。`text()` メソッドを使って `text` オブジェクトを作成し、`ax1` オブジェクトに追加します。次に、`add_artist()` メソッドを使って `BboxImage` オブジェクトを作成します。`text` オブジェクトの `get_window_extent` メソッドを `BboxImage` コンストラクタに渡して、テキストのバウンディングボックスを取得します。また、`BboxImage` コンストラクタの `data` パラメータに形状 (1, 256) の 1 次元配列を渡して画像を作成します。

```python
fig, (ax1, ax2) = plt.subplots(ncols=2)

txt = ax1.text(0.5, 0.5, "test", size=30, ha="center", color="w")
ax1.add_artist(
    BboxImage(txt.get_window_extent, data=np.arange(256).reshape((1, -1))))
```
