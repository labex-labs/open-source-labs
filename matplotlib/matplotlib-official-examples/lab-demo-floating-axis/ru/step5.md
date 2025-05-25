# Создаем плавающие оси

В этом шаге мы создадим две плавающие оси, которые будут использоваться для отображения полярной кривой в прямоугольном框。Для создания плавающих осей мы будем использовать `new_floating_axis()`.

```python
# Create the floating axes
ax1.axis["lat"] = axis = ax1.new_floating_axis(0, 60)
axis.label.set_text(r"$\theta = 60^{\circ}$")
axis.label.set_visible(True)

ax1.axis["lon"] = axis = ax1.new_floating_axis(1, 6)
axis.label.set_text(r"$r = 6$")
```

需注意，你原文中“rectangular box”表述不太准确，这里直接按字面翻译为“框”，你可根据实际情况调整。
