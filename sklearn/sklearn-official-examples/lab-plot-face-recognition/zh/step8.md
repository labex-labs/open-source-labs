# 可视化特征脸

```python
eigenface_titles = ["特征脸 %d" % i for i in range(eigenfaces.shape[0])]
plot_gallery(eigenfaces, eigenface_titles, h, w)

plt.show()
```

我们还绘制特征脸，以可视化从输入数据中提取的特征。
