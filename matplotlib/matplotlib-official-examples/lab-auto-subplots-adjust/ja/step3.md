# 描画コールバック関数を定義する

グラフが描画されるたびに呼び出される関数を定義します。この関数は、y 軸のラベルの境界ボックスを計算し、サブプロットがラベルに十分なスペースを残しているかどうかを判断し、必要に応じてサブプロットのパラメータを調整します。

```python
def on_draw(event):
    bboxes = []
    for label in ax.get_yticklabels():
        # ピクセル単位の境界ボックス
        bbox_px = label.get_window_extent()
        # 相対的なグラフ座標に変換します。これは transFigure の逆変換です。
        bbox_fig = bbox_px.transformed(fig.transFigure.inverted())
        bboxes.append(bbox_fig)
    # すべての bbox を囲む bbox、再び相対的なグラフ座標で
    bbox = mtransforms.Bbox.union(bboxes)
    if fig.subplotpars.left < bbox.width:
        # サブプロットの左辺を右にもっと移動させます
        fig.subplots_adjust(left=1.1*bbox.width)  # 少し余白を空けます
        fig.canvas.draw()
```
