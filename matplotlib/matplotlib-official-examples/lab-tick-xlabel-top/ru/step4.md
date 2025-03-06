# Дальнейшая настройка графика

Теперь, когда мы переместили метки делений оси x вверх, давайте еще больше настроим наш график, чтобы сделать его более визуально привлекательным и информативным.

## Продвинутые методы настройки графиков

Matplotlib предлагает множество вариантов для настройки графиков. Исследуем некоторые из них:

```python
# Create a new figure and a set of axes
fig, ax = plt.subplots(figsize=(10, 6))

# Generate some data with more points for a smoother curve
x = np.linspace(0, 2*np.pi, 100)
y1 = np.sin(x)
y2 = np.cos(x)

# Plot multiple datasets
ax.plot(x, y1, linewidth=2, color='blue', label='sin(x)')
ax.plot(x, y2, linewidth=2, color='red', label='cos(x)')

# Fill the area between curves
ax.fill_between(x, y1, y2, where=(y1 > y2), alpha=0.3, color='green', interpolate=True)
ax.fill_between(x, y1, y2, where=(y1 <= y2), alpha=0.3, color='purple', interpolate=True)

# Move the x-axis tick labels to the top
ax.tick_params(
    axis='x',
    top=True,
    labeltop=True,
    bottom=False,
    labelbottom=False
)

# Customize tick labels
ax.set_xticks(np.arange(0, 2*np.pi + 0.1, np.pi/2))
ax.set_xticklabels(['0', 'π/2', 'π', '3π/2', '2π'])

# Add title and labels with custom styles
ax.set_title('Sine and Cosine Functions with Customized X-Axis Labels at the Top',
             fontsize=14, fontweight='bold', pad=20)
ax.set_xlabel('Angle (radians)', fontsize=12)
ax.set_ylabel('Function Value', fontsize=12)

# Add a grid and customize its appearance
ax.grid(True, linestyle='--', alpha=0.7, which='both')

# Customize the axis limits
ax.set_ylim(-1.2, 1.2)

# Add a legend with custom location and style
ax.legend(loc='upper right', fontsize=12, framealpha=0.8)

# Add annotations to highlight important points
ax.annotate('Maximum', xy=(np.pi/2, 1), xytext=(np.pi/2, 1.1),
            arrowprops=dict(facecolor='black', shrink=0.05, width=1.5),
            fontsize=10, ha='center')

# Display the plot
plt.tight_layout()  # Adjust spacing for better appearance
plt.show()

print("We have created a fully customized plot with x-axis tick labels at the top!")
```

При запуске этого кода вы увидите гораздо более сложный и профессионально выглядящий график с:

- Двумя кривыми (синусом и косинусом)
- Цветными областями между кривыми
- Пользовательскими метками делений (с использованием обозначения π)
- Аннотациями, указывающими на важные особенности
- Лучшим расположением и стилем

Обратите внимание, как мы сохранили метки делений оси x вверху с помощью метода `tick_params()`, но улучшили график с помощью дополнительных настроек.

## Понимание настроек

Разберем некоторые важные настройки, которые мы добавили:

1. `fill_between()`: Создает цветные области между кривыми синуса и косинуса.
2. `set_xticks()` и `set_xticklabels()`: Настраивают позиции и метки делений.
3. `tight_layout()`: Автоматически настраивает отступы на графике для лучшего вида.
4. `annotate()`: Добавляет текст с стрелкой, указывающей на определенную точку.
5. Настроенные шрифты, цвета и стили для различных элементов.

Эти настройки показывают, как можно создавать визуально привлекательные и информативные графики, сохраняя при этом метки делений оси x вверху.
