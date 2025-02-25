# Использование прозрачности для выделения значений

Наконец, мы снова построим такой же график, но на этот раз мы будем использовать прозрачность для выделения экстремальных значений в данных. Это часто используется для выделения точек данных с меньшими p-значениями. Мы также добавим контурные линии, чтобы выделить значения изображения.

```python
# Create an alpha channel based on weight values
alphas = Normalize(0,.3, clip=True)(np.abs(weights))
alphas = np.clip(alphas,.4, 1)  # alpha value clipped at the bottom at.4

# Create the figure and image
fig, ax = plt.subplots()
ax.imshow(greys)
ax.imshow(weights, alpha=alphas, **imshow_kwargs)

# Add contour lines to further highlight different levels.
ax.contour(weights[::-1], levels=[-.1,.1], colors='k', linestyles='-')
ax.set_axis_off()
plt.show()

ax.contour(weights[::-1], levels=[-.0001,.0001], colors='k', linestyles='-')
ax.set_axis_off()
plt.show()
```
