# Создание переиспользуемой функции для наложения изображений

Для того чтобы сделать наш код более переиспользуемым, давайте создадим функцию, которая может добавить наложение изображения на любую фигуру Matplotlib. Таким образом, мы сможем легко применить тот же эффект к разным графикам.

1. Создайте новую ячейку в своем ноутбуке и введите следующий код:

```python
def add_image_overlay(fig, image_path, x_pos=25, y_pos=25, alpha=0.5, zorder=3):
    """
    Add an image overlay to a matplotlib figure.

    Parameters:
    -----------
    fig : matplotlib.figure.Figure
        The figure to add the image to
    image_path : str
        Path to the image file
    x_pos : int
        X position in pixels from the bottom left
    y_pos : int
        Y position in pixels from the bottom left
    alpha : float
        Transparency level (0 to 1)
    zorder : int
        Drawing order (higher numbers are drawn on top)

    Returns:
    --------
    fig : matplotlib.figure.Figure
        The figure with the image overlay
    """
    # Load the image
    with cbook.get_sample_data(image_path) as file:
        im = image.imread(file)

    # Add the image to the figure
    fig.figimage(im, x_pos, y_pos, zorder=zorder, alpha=alpha)

    return fig

# Example usage: Create a scatter plot with an image overlay
fig, ax = plt.subplots(figsize=(10, 6))

# Set a random seed for reproducibility
np.random.seed(19680801)

# Generate random data for a scatter plot
x = np.random.rand(50) * 10
y = np.random.rand(50) * 10

# Create a scatter plot
ax.scatter(x, y, s=100, c=np.random.rand(50), cmap='viridis', alpha=0.7)
ax.grid(linestyle='--', alpha=0.7)
ax.set_xlabel('X-axis Label')
ax.set_ylabel('Y-axis Label')
ax.set_title('Scatter Plot with Image Overlay')

# Add the image overlay using our function
add_image_overlay(fig, 'logo2.png', x_pos=50, y_pos=50, alpha=0.4)

# Display the plot
plt.tight_layout()
plt.show()
```

Этот код определяет функцию `add_image_overlay`, которая:

- Принимает параметры для фигуры, пути к изображению, позиции, прозрачности и z-порядка.
- Загружает указанное изображение.
- Добавляет изображение на фигуру с использованием `figimage`.
- Возвращает модифицированную фигуру.

После определения функции мы демонстрируем ее использование, создав точечную диаграмму с случайными данными и добавив логотип Matplotlib в виде наложения.

2. Запустите ячейку, нажав Shift+Enter.

В выводе должна отобразиться точечная диаграмма с случайно расположенными и окрашенными точками, а также логотип Matplotlib, наложенный в позиции (50, 50) с прозрачностью 40%.

3. Попробуем еще один пример с линейным графиком. Создайте новую ячейку и введите следующий код:

```python
# Example usage: Create a line plot with an image overlay
fig, ax = plt.subplots(figsize=(10, 6))

# Generate data for a line plot
x = np.linspace(0, 10, 100)
y = np.sin(x)

# Create a line plot
ax.plot(x, y, linewidth=2, color='#d62728')
ax.grid(linestyle='--', alpha=0.7)
ax.set_xlabel('X-axis Label')
ax.set_ylabel('Y-axis Label')
ax.set_title('Sine Wave with Image Overlay')
ax.set_ylim(-1.5, 1.5)

# Add the image overlay using our function
# Place it in the bottom right corner
fig_width, fig_height = fig.get_size_inches() * fig.dpi
with cbook.get_sample_data('logo2.png') as file:
    im = image.imread(file)
    x_pos = fig_width - im.shape[1] - 50  # 50 pixels from the right edge

add_image_overlay(fig, 'logo2.png', x_pos=x_pos, y_pos=50, alpha=0.6)

# Display the plot
plt.tight_layout()
plt.show()
```

Этот код создает линейный график, показывающий синусоиду, и добавляет логотип Matplotlib в нижний правый угол графика.

4. Запустите ячейку, нажав Shift+Enter.

В выводе должна отобразиться линейный график синусоиды с логотипом Matplotlib, наложенным в нижнем правом углу с прозрачностью 60%.

Эти примеры демонстрируют, как функция `add_image_overlay` может быть использована для легкого добавления наложений изображений к разным типам графиков, делая ее универсальным инструментом для настройки визуализаций.
