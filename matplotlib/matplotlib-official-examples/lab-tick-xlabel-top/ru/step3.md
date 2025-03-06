# Перемещение меток делений оси X вверх

Теперь, когда мы понимаем, как располагаются метки делений по умолчанию, давайте переместим метки делений оси x в верхнюю часть графика.

## Понимание параметров делений

Matplotlib предоставляет метод `tick_params()`, чтобы управлять внешним видом делений и меток делений. Этот метод позволяет нам:

- Показывать/скрывать деления и метки делений
- Изменять их положение (сверху, снизу, слева, справа)
- Настраивать их размер, цвет и другие свойства

## Создание графика с метками делений оси X вверху

Создадим новый график с метками делений оси x, перемещенными вверх:

```python
# Create a new figure and a set of axes
fig, ax = plt.subplots(figsize=(8, 5))

# Generate some data
x = np.arange(0, 10, 1)
y = np.cos(x)

# Plot the data
ax.plot(x, y, marker='s', linestyle='-', color='green', label='cos(x)')

# Move the x-axis tick labels to the top
ax.tick_params(
    axis='x',         # Apply changes to the x-axis
    top=True,         # Show ticks on the top side
    labeltop=True,    # Show tick labels on the top side
    bottom=False,     # Hide ticks on the bottom side
    labelbottom=False # Hide tick labels on the bottom side
)

# Add a title and labels
ax.set_title('Cosine Wave with X-Axis Tick Labels at the Top')
ax.set_xlabel('X-axis (now at the top!)')
ax.set_ylabel('Y-axis (cos(x))')

# Add a grid and legend
ax.grid(True, linestyle='--', alpha=0.7)
ax.legend()

# Display the plot
plt.show()

print("Now the x-axis tick labels are at the top of the plot!")
```

При запуске этого кода вы увидите график косинуса с метками делений оси x в верхней части графика.

Обратите внимание, как метод `tick_params()` используется с несколькими параметрами:

- `axis='x'`: Указывает, что мы хотим изменить ось x.
- `top=True` и `labeltop=True`: Делает деления и метки делений видимыми сверху.
- `bottom=False` и `labelbottom=False`: Скрывает деления и метки делений снизу.

Это позволяет нам получить чистый вид данных с метками оси x, расположенными сверху, а не снизу.
