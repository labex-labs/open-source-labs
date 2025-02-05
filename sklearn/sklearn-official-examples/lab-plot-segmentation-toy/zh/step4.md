# 绘制结果

我们将使用 `matplotlib.pyplot` 中的 `matshow` 并排绘制原始图像和分割后的图像。

```python
import matplotlib.pyplot as plt

label_im = np.full(mask.shape, -1.0)
label_im[mask] = labels

fig, axs = plt.subplots(nrows=1, ncols=2, figsize=(10, 5))
axs[0].matshow(img)
axs[1].matshow(label_im)

plt.show()
```
