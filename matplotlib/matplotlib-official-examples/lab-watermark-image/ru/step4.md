# Наложение изображения на график

Теперь, когда мы создали базовый график, давайте наложим на него изображение. Мы будем использовать метод `figimage` для добавления изображения на фигуру и сделаем его полупрозрачным, чтобы нижележащий график оставался видимым.

1. Создайте новую ячейку в своем ноутбуке и введите следующий код:

```python
# Create a figure and axes for our plot (same as before)
fig, ax = plt.subplots(figsize=(10, 6))

# Set a random seed for reproducibility
np.random.seed(19680801)

# Generate random data
x = np.arange(30)  # x-axis values (0 to 29)
y = x + np.random.randn(30)  # y-axis values (x plus random noise)

# Create a bar chart
bars = ax.bar(x, y, color='#6bbc6b')  # Green bars

# Add grid lines
ax.grid(linestyle='--', alpha=0.7)

# Add labels and title
ax.set_xlabel('X-axis Label')
ax.set_ylabel('Y-axis Label')
ax.set_title('Bar Chart with Image Overlay')

# Load the image
with cbook.get_sample_data('logo2.png') as file:
    im = image.imread(file)

# Overlay the image on the plot
# Parameters:
# - im: the image data
# - 25, 25: x and y position in pixels from the bottom left
# - zorder=3: controls the drawing order (higher numbers are drawn on top)
# - alpha=0.5: controls the transparency (0 = transparent, 1 = opaque)
fig.figimage(im, 25, 25, zorder=3, alpha=0.5)

# Display the plot
plt.tight_layout()
plt.show()
```

Этот код объединяет действия, выполненные на предыдущих шагах, и добавляет метод `figimage` для наложения изображения на график. Вот разбор параметров метода `figimage`:

- `im`: Данные изображения в виде массива NumPy.
- `25, 25`: Координаты x и y в пикселях от нижнего левого угла фигуры.
- `zorder = 3`: Управляет порядком рисования. Более высокие значения рисуются поверх элементов с более низкими значениями.
- `alpha = 0.5`: Управляет прозрачностью изображения. Значение 0 означает полную прозрачность, а 1 - полную непрозрачность.

2. Запустите ячейку, нажав Shift+Enter.

В выводе должна отобразиться та же столбчатая диаграмма, что и раньше, но теперь с наложенным логотипом Matplotlib в нижнем левом углу. Логотип должен быть полупрозрачным, чтобы нижележащий график оставался видимым.

3. Давайте поэкспериментируем с разными положениями и уровнями прозрачности. Создайте новую ячейку и введите следующий код:

```python
# Create a figure and axes for our plot
fig, ax = plt.subplots(figsize=(10, 6))

# Set a random seed for reproducibility
np.random.seed(19680801)

# Generate random data
x = np.arange(30)
y = x + np.random.randn(30)

# Create a bar chart
bars = ax.bar(x, y, color='#6bbc6b')
ax.grid(linestyle='--', alpha=0.7)
ax.set_xlabel('X-axis Label')
ax.set_ylabel('Y-axis Label')
ax.set_title('Bar Chart with Centered Image Overlay')

# Load the image
with cbook.get_sample_data('logo2.png') as file:
    im = image.imread(file)

# Get figure dimensions
fig_width, fig_height = fig.get_size_inches() * fig.dpi

# Calculate center position (this is approximate)
x_center = fig_width / 2 - im.shape[1] / 2
y_center = fig_height / 2 - im.shape[0] / 2

# Overlay the image at the center with higher transparency
fig.figimage(im, x_center, y_center, zorder=3, alpha=0.3)

# Display the plot
plt.tight_layout()
plt.show()
```

Этот код размещает изображение в центре фигуры с более высоким уровнем прозрачности (alpha = 0.3), что делает его более подходящим в качестве водяного знака.

4. Запустите ячейку, нажав Shift+Enter.

В выводе должна отобразиться столбчатая диаграмма с логотипом, расположенным по центру и более прозрачным, чем раньше, создавая эффект водяного знака.
