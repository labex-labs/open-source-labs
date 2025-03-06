# Сохранение графика и создание переиспользуемой функции

На этом последнем этапе мы создадим переиспользуемую функцию для генерации графиков с форматированием денежных значений и сохраним нашу визуализацию в файл. Такой подход позволит легко применять то же форматирование к разным финансовым наборам данных в будущем.

В новой ячейке вашего блокнота добавьте и запустите следующий код:

```python
def create_currency_plot(x_data, y_data, title='Financial Data',
                         xlabel='X-Axis', ylabel='Amount ($)',
                         filename=None, show_stats=True):
    """
    Create a plot with currency formatting on the y-axis.

    Parameters:
    -----------
    x_data : array-like
        Data for the x-axis
    y_data : array-like
        Data for the y-axis (currency values)
    title : str
        Title of the plot
    xlabel : str
        Label for the x-axis
    ylabel : str
        Label for the y-axis
    filename : str, optional
        If provided, save the plot to this filename
    show_stats : bool
        Whether to show statistics (average, min, max)

    Returns:
    --------
    fig, ax : tuple
        The figure and axes objects
    """
    # Import the necessary module for formatting
    import matplotlib.ticker as ticker

    # Create a figure and axes
    fig, ax = plt.subplots(figsize=(12, 7))

    # Plot the data
    ax.plot(x_data, y_data, marker='o', linestyle='-', color='blue',
            linewidth=2, markersize=6, label='Data')

    if show_stats:
        # Calculate statistics
        avg_value = np.mean(y_data)
        max_value = np.max(y_data)
        min_value = np.min(y_data)
        max_x = x_data[np.argmax(y_data)]
        min_x = x_data[np.argmin(y_data)]

        # Add a horizontal line for average value
        ax.axhline(y=avg_value, color='r', linestyle='--', alpha=0.7,
                   label=f'Average: ${avg_value:.2f}')

        # Add annotations for max and min values
        ax.annotate(f'Max: ${max_value:.2f}', xy=(max_x, max_value),
                    xytext=(max_x+1, max_value+200),
                    arrowprops=dict(facecolor='black', shrink=0.05, width=1.5))

        ax.annotate(f'Min: ${min_value:.2f}', xy=(min_x, min_value),
                    xytext=(min_x+1, min_value-200),
                    arrowprops=dict(facecolor='black', shrink=0.05, width=1.5))

    # Format y-axis with dollar signs
    formatter = ticker.StrMethodFormatter('${x:,.2f}')
    ax.yaxis.set_major_formatter(formatter)

    # Customize tick parameters
    ax.tick_params(axis='both', which='major', labelsize=10)

    # Add labels and title
    ax.set_xlabel(xlabel, fontsize=12)
    ax.set_ylabel(ylabel, fontsize=12)
    ax.set_title(title, fontsize=14, fontweight='bold')

    # Add grid for better readability
    ax.grid(True, linestyle='--', alpha=0.7)

    # Add legend
    if show_stats:
        ax.legend(loc='best', fontsize=10)

    # Adjust layout
    plt.tight_layout()

    # Save the plot if filename is provided
    if filename:
        plt.savefig(filename, dpi=300, bbox_inches='tight')
        print(f"Plot saved as '{filename}'")

    return fig, ax

# Use our function to create and save a plot
fig, ax = create_currency_plot(
    days,
    daily_revenue,
    title='Monthly Revenue Report',
    xlabel='Day of Month',
    ylabel='Daily Revenue ($)',
    filename='revenue_plot.png'
)

# Display the plot
plt.show()

print("Function created and plot saved successfully!")
```

После запуска этого кода вы должны увидеть:

1. График, аналогичный тому, который мы создали на предыдущем этапе, но сгенерированный с использованием нашей пользовательской функции.
2. Сообщение, подтверждающее, что график был сохранен в файл с именем `revenue_plot.png`.

Созданная нами функция:

- Принимает данные для осей X и Y.
- Позволяет настраивать метки и заголовок.
- Имеет возможность сохранить график в файл.
- Может отображать или скрывать статистические показатели, такие как среднее, минимальное и максимальное значения.
- Возвращает объекты фигуры и осей для дальнейшей настройки при необходимости.

Эта переиспользуемая функция позволяет легко создавать финансовые графики с единообразным форматированием в будущем. Вы можете просто вызвать эту функцию с разными наборами данных, и она автоматически обработает все форматирование денежных значений и статистические аннотации.

Чтобы убедиться, что наш график был сохранен правильно, проверим, существует ли файл:

```python
import os
if os.path.exists('revenue_plot.png'):
    print("Plot file exists! Size:", os.path.getsize('revenue_plot.png'), "bytes")
else:
    print("Plot file was not saved correctly.")
```

Вы должны увидеть сообщение, подтверждающее существование файла и его размер.

Поздравляем! Вы успешно научились форматировать графики с использованием знаков доллара и создавать профессионально выглядящие финансовые визуализации с помощью Matplotlib.
