# Отобразить изображение с магнитно-резонансной томографии (МРТ)

Мы будем использовать функцию `imshow` из `matplotlib` для отображения изображения с МРТ в оттенках серого.

```python
fig, ax = plt.subplots(num="MRI_demo")
ax.imshow(im, cmap="gray")
ax.axis('off')
plt.show()
```
