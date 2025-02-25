# Создаем график с вертикальной цветовой полосой

Начнем с создания графика с вертикальной цветовой полосой. Сгенерируем некоторые случайные данные с использованием `randn` из `numpy` и обрежем значения до диапазона от -1 до 1. Затем создадим объект `AxesImage` с использованием `imshow` и цветовой карты `coolwarm`. Наконец, добавим заголовок к графику.

```python
# Make plot with vertical (default) colorbar
fig, ax = plt.subplots()

data = np.clip(randn(250, 250), -1, 1)

cax = ax.imshow(data, cmap=cm.coolwarm)
ax.set_title('Gaussian noise with vertical colorbar')
```
