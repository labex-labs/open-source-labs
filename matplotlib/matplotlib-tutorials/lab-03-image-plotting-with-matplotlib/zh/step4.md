# 添加颜色刻度参考

为了给颜色刻度提供参考，我们可以在绘图中添加一个颜色条。这可以使用 `matplotlib.pyplot` 中的 `colorbar` 函数来完成。

```python
imgplot = plt.imshow(lum_img)
plt.colorbar()
```
