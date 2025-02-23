# 画像の拡大縮小と反射を行う

このステップでは、`scale`関数を使って画像の拡大縮小と反射を行います。拡大縮小と反射の係数を`scale`関数の入力として渡します。拡大縮小と反射された画像を表示するために`do_plot`関数を使います。

```python
# prepare image and figure
fig, ax3 = plt.subplots()
Z = get_image()

# scale and reflection
do_plot(ax3, Z, mtransforms.Affine2D().scale(-1,.5))
```
