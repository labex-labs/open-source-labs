# グラフと ImageGrid を作成する

次に、グリッドの行数と列数を定義するための`nrows_ncols`パラメータを使用して、グラフと ImageGrid を作成します。

```python
fig = plt.figure(figsize=(5.5, 3.5))
grid = ImageGrid(fig, 111,  # similar to subplot(111)
                 nrows_ncols=(1, 3),
                 axes_pad=0.1,
                 label_mode="L")
```
