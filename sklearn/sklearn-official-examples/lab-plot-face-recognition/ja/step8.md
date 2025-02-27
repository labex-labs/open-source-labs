# 固有顔（Eigenfaces）の可視化

```python
eigenface_titles = ["eigenface %d" % i for i in range(eigenfaces.shape[0])]
plot_gallery(eigenfaces, eigenface_titles, h, w)

plt.show()
```

また、入力データから抽出された特徴を可視化するために、固有顔（eigenfaces）を描画します。
