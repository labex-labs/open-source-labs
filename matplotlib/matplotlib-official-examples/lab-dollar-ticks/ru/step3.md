# Форматирование меток оси Y с использованием знаков доллара

Теперь, когда у нас есть базовый график, давайте отформатируем метки оси Y так, чтобы они отображали знаки доллара. Это сделает наши финансовые данные более читаемыми и профессионально выглядящими.

Для форматирования делений на оси Y мы будем использовать модуль `ticker` библиотеки Matplotlib, который предоставляет различные варианты форматирования. В частности, мы воспользуемся классом `StrMethodFormatter` для создания настраиваемого форматтера для нашей оси Y.

В новой ячейке вашего блокнота добавьте и запустите следующий код:

```python
# Import the necessary module for formatting
import matplotlib.ticker as ticker

# Create a figure and axes
fig, ax = plt.subplots(figsize=(10, 6))

# Plot the daily revenue data
ax.plot(days, daily_revenue, marker='o', linestyle='-', color='blue', linewidth=2, markersize=6)

# Format y-axis with dollar signs
formatter = ticker.StrMethodFormatter('${x:,.2f}')
ax.yaxis.set_major_formatter(formatter)

# Add labels and title
ax.set_xlabel('Day', fontsize=12)
ax.set_ylabel('Revenue ($)', fontsize=12)
ax.set_title('Daily Revenue Over 30 Days', fontsize=14, fontweight='bold')

# Add grid for better readability
ax.grid(True, linestyle='--', alpha=0.7)

# Display the plot
plt.tight_layout()
plt.show()

print("Plot with dollar-formatted y-axis created!")
```

После запуска этого кода вы должны увидеть новый график с знаками доллара на метках оси Y.

Давайте объясним ключевую часть этого кода:

```python
formatter = ticker.StrMethodFormatter('${x:,.2f}')
ax.yaxis.set_major_formatter(formatter)
```

Вот что делает эта строка форматирования:

- `$` - Добавляет знак доллара в начале каждой метки
- `{x:,.2f}` - Форматирует число следующим образом:
  - `,` - Использует запятую как разделитель тысяч (например, 1 000 вместо 1000)
  - `.2f` - Округляет число до двух знаков после запятой (например, $1 234,56)

Этот форматтер применяется ко всем основным делениям на оси Y. Обратите внимание, как график теперь четко показывает, что значения даны в долларах, что делает его гораздо более подходящим для визуализации финансовых данных.
