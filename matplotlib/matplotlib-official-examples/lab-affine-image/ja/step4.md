# 画像の歪みを行う

このステップでは、`skew_deg`関数を使って画像の歪みを行います。歪み角度を`skew_deg`関数の入力として渡します。歪んだ画像を表示するために`do_plot`関数を使います。

```python
# prepare image and figure
fig, ax2 = plt.subplots()
Z = get_image()

# image skew
do_plot(ax2, Z, mtransforms.Affine2D().skew_deg(30, 15))
```
