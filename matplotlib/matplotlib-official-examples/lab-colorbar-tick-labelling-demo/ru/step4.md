# Создаем график с горизонтальной цветовой полосой

Теперь мы создадим график с горизонтальной цветовой полосой. Будем следовать тем же шагам, что и в шаге 2, но на этот раз будем использовать цветовую карту `afmhot` и установим ориентацию цветовой полосы горизонтальной.

```python
# Make plot with horizontal colorbar
fig, ax = plt.subplots()

data = np.clip(randn(250, 250), -1, 1)

cax = ax.imshow(data, cmap=cm.afmhot)
ax.set_title('Gaussian noise with horizontal colorbar')

cbar = fig.colorbar(cax, ticks=[-1, 0, 1], orientation='horizontal')
cbar.ax.set_xticklabels(['Low', 'Medium', 'High'])  # horizontal colorbar
```
