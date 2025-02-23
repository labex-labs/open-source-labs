# 画像の回転を行う

このステップでは、`rotate_deg`関数を使って画像を回転させます。回転角度を`rotate_deg`関数の入力として渡します。回転させた画像を表示するために`do_plot`関数を使います。

```python
# prepare image and figure
fig, ax1 = plt.subplots()
Z = get_image()

# image rotation
do_plot(ax1, Z, mtransforms.Affine2D().rotate_deg(30))
```
