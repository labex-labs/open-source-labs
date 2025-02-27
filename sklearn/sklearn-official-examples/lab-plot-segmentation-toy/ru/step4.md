# Построение результатов

Мы построим исходное изображение и сегментированное изображение рядом с использованием `matshow` из `matplotlib.pyplot`.

```python
import matplotlib.pyplot as plt

label_im = np.full(mask.shape, -1.0)
label_im[mask] = labels

fig, axs = plt.subplots(nrows=1, ncols=2, figsize=(10, 5))
axs[0].matshow(img)
axs[1].matshow(label_im)

plt.show()
```
