# 显示MRI图像

我们将使用`matplotlib`中的`imshow`函数以灰度显示MRI图像。

```python
fig, ax = plt.subplots(num="MRI_demo")
ax.imshow(im, cmap="gray")
ax.axis('off')
plt.show()
```
