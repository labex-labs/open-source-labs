# 绘制 MRI 强度直方图

接下来，我们将使用 `hist()` 函数绘制 MRI 强度的直方图。我们会将强度值归一化到 0 到 1 的范围。

```python
# 绘制 MRI 强度直方图
ax1 = fig.add_subplot(2, 2, 2)
im = np.ravel(im)
im = im[np.nonzero(im)]  # 忽略背景
im = im / im.max()  # 归一化
ax1.hist(im, bins=100)
ax1.set_xlabel('Intensity (a.u.)')
ax1.set_ylabel('MRI density')
```
