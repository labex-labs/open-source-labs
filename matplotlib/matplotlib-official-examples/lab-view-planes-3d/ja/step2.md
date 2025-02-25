# 軸に注釈を付ける関数を定義する

後で各一次3Dビュープレーンにそれぞれの角度を付ける注釈を付けるために使用する`annotate_axes`関数を定義します。

```python
def annotate_axes(ax, text, fontsize=18):
    ax.text(x=0.5, y=0.5, z=0.5, s=text,
            va="center", ha="center", fontsize=fontsize, color="black")
```
