# Создание базового финансового графика

Теперь, когда наши данные готовы, давайте создадим базовый график для визуализации ежедневной выручки. Мы начнем с простого линейного графика, который покажет тенденцию выручки за 30 - дневный период.

В новой ячейке вашего блокнота добавьте и запустите следующий код:

```python
# Create a figure and axes
fig, ax = plt.subplots(figsize=(10, 6))

# Plot the daily revenue data
ax.plot(days, daily_revenue, marker='o', linestyle='-', color='blue', linewidth=2, markersize=6)

# Add labels and title
ax.set_xlabel('Day', fontsize=12)
ax.set_ylabel('Revenue', fontsize=12)
ax.set_title('Daily Revenue Over 30 Days', fontsize=14, fontweight='bold')

# Add grid for better readability
ax.grid(True, linestyle='--', alpha=0.7)

# Display the plot
plt.tight_layout()
plt.show()

print("Basic plot created successfully!")
```

После запуска этого кода вы должны увидеть линейный график, показывающий тенденцию ежедневной выручки. Он должен выглядеть приблизительно так (фактические значения могут немного отличаться из - за случайной генерации):

![Basic Revenue Plot](../assets/screenshot-20250306-ywFsL4VH@2x.png)

Давайте разберем, что мы сделали в этом коде:

1. `fig, ax = plt.subplots(figsize=(10, 6))` - Создали фигуру и оси размером 10×6 дюймов
2. `ax.plot(days, daily_revenue, ...)` - Построили наш график с днями по оси X и выручкой по оси Y
3. `ax.set_xlabel()`, `ax.set_ylabel()`, `ax.set_title()` - Добавили подписи и заголовок к нашему графику
4. `ax.grid()` - Добавили сетку, чтобы данные были легче читать
5. `plt.tight_layout()` - Подкрепили отступы, чтобы все было расположено красиво
6. `plt.show()` - Отобразили график

Обратите внимание, что на оси Y в настоящее время отображаются простые числа без знаков доллара. На следующем шаге мы изменим наш график, чтобы на оси Y отображался правильный денежный формат.
