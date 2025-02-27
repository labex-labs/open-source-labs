# Визуализация ранжирования признаков

Наконец, мы построим график ранжирования признаков с использованием библиотеки Matplotlib. Мы будем использовать функцию `matshow()`, чтобы отобразить ранжирование в виде изображения. Также добавим цветовую шкалу и заголовок к графику.

```python
import matplotlib.pyplot as plt

plt.matshow(ranking, cmap=plt.cm.Blues)
plt.colorbar()
plt.title("Ranking of pixels with RFE")
plt.show()
```
