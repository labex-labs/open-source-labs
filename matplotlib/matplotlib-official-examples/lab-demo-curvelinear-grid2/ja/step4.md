# 軸を定義して画像を表示する

4番目のステップは、3番目のステップで作成した`grid_helper`インスタンスを使って軸を定義することです。また、`imshow`関数を使って画像を表示します。

```python
ax1 = fig.add_subplot(axes_class=Axes, grid_helper=grid_helper)
ax1.imshow(np.arange(25).reshape(5, 5), vmax=50, cmap=plt.cm.gray_r, origin="lower")
```
