# グラフとImageGridオブジェクトを作成する

次に、`plt.figure`関数を使って`figure`オブジェクトを作成し、`figsize`引数を指定してグラフのサイズを設定します。その後、`ImageGrid`関数を使って`ImageGrid`オブジェクトを作成し、`figure`、サブプロット引数として`111`、`nrows_ncols`引数として`(2, 2)`を指定して2x2の軸のグリッドを作成し、軸間のパディングを設定するために`axes_pad`引数として`0.1`を指定します。

```python
fig = plt.figure(figsize=(4., 4.))
grid = ImageGrid(fig, 111, nrows_ncols=(2, 2), axes_pad=0.1)
```
