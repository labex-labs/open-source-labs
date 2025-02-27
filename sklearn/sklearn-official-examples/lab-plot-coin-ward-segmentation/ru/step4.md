# Построение результатов

Наконец, мы можем построить результаты на изображении. Мы будем использовать matplotlib для построения масштабированного изображения и контуров кластеров. Мы будем перебирать каждый кластер и рисовать контур пикселей в этом кластере.

```python
import matplotlib.pyplot as plt

plt.figure(figsize=(5, 5))
plt.imshow(rescaled_coins, cmap=plt.cm.gray)
for l in range(n_clusters):
    plt.contour(
        label == l,
        colors=[
            plt.cm.nipy_spectral(l / float(n_clusters)),
        ],
    )
plt.axis("off")
plt.show()
```
