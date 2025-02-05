# 计算小波字典

我们将计算一个小波字典，并使用 Matplotlib 对其进行可视化。

```python
# 计算一个小波字典
D_fixed = ricker_matrix(width=width, resolution=resolution, n_components=n_components)
D_multi = np.r_[
    tuple(
        ricker_matrix(width=w, resolution=resolution, n_components=n_components // 5)
        for w in (10, 50, 100, 500, 1000)
    )
]

# 可视化小波字典
plt.figure(figsize=(10, 5))
for i, D in enumerate((D_fixed, D_multi)):
    plt.subplot(1, 2, i + 1)
    plt.imshow(D, cmap=plt.cm.gray, interpolation="nearest")
    plt.title("小波字典 (%s)" % ("固定宽度" if i == 0 else "多种宽度"))
    plt.axis("off")
plt.show()
```
