# 複数の変換を行う

このステップでは、`rotate_deg`、`skew_deg`、`scale`、および`translate`関数を使って画像に複数の変換を行います。変換パラメータをそれぞれの関数の入力として渡します。変換された画像を表示するために`do_plot`関数を使います。

```python
# prepare image and figure
fig, ax4 = plt.subplots()
Z = get_image()

# everything and a translation
do_plot(ax4, Z, mtransforms.Affine2D().
        rotate_deg(30).skew_deg(30, 15).scale(-1,.5).translate(.5, -1))
```
