# Построим круг с неравномерным соотношением сторон осей

Сначала построим круг с неравномерным соотношением сторон осей, чтобы продемонстрировать важность установки равных соотношений сторон осей.

```python
an = np.linspace(0, 2 * np.pi, 100)
fig, axs = plt.subplots(2, 2)

axs[0, 0].plot(3 * np.cos(an), 3 * np.sin(an))
axs[0, 0].set_title('not equal, looks like ellipse', fontsize=10)
```

В результирующем графике будет показан круг, который выглядит удлиненным из-за неравномерного соотношения сторон осей.
