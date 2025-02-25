# カラースケールの参照の追加

カラースケールの参照を提供するには、プロットにカラーバーを追加できます。これは `matplotlib.pyplot` の `colorbar` 関数を使って行うことができます。

```python
imgplot = plt.imshow(lum_img)
plt.colorbar()
```
