# Создаем заполненный контур с автоматическими уровнями

Далее мы создадим заполненный контурный график с автоматическими уровнями. Мы будем использовать метод `contourf` с параметром `cmap`, установленным на `plt.cm.bone`, чтобы указать карту цветов. Мы также добавим контурные линии с помощью метода `contour` и передадим подмножество уровней контура, используемых для заполненных контуров.

```python
# Create filled contour with automatic levels
fig, ax = plt.subplots()
CS = ax.contourf(X, Y, Z, 10, cmap=plt.cm.bone, origin=origin)
CS2 = ax.contour(CS, levels=CS.levels[::2], colors='r', origin=origin)

# Add title, axis labels, and colorbar
ax.set_title('Filled Contour with Automatic Levels')
ax.set_xlabel('X Label')
ax.set_ylabel('Y Label')
cbar = fig.colorbar(CS)
cbar.ax.set_ylabel('Z Label')
cbar.add_lines(CS2)

# Show plot
plt.show()
```
