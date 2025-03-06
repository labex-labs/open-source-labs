# Настройка текстового блока

Теперь, когда мы успешно добавили текстовый блок к нашему графику, исследуем различные параметры настройки, чтобы сделать его более визуально привлекательным и подходящим для разных контекстов.

## Эксперименты с разными стилями

Создадим функцию, чтобы упростить эксперименты с разными стилями текстовых блоков. В новой ячейке введите и запустите следующий код:

```python
def plot_with_textbox(boxstyle, facecolor, alpha, position=(0.05, 0.95)):
    """
    Create a histogram with a custom text box.

    Parameters:
    boxstyle (str): Style of the box ('round', 'square', 'round4', etc.)
    facecolor (str): Background color of the box
    alpha (float): Transparency of the box (0-1)
    position (tuple): Position of the box in axes coordinates (x, y)
    """
    # Create figure and plot
    fig, ax = plt.subplots(figsize=(8, 5))
    ax.hist(x, bins=50, color='skyblue', edgecolor='black')

    # Set title and labels
    ax.set_title(f'Text Box Style: {boxstyle}', fontsize=16)
    ax.set_xlabel('Value', fontsize=12)
    ax.set_ylabel('Frequency', fontsize=12)

    # Create text box properties
    box_props = dict(boxstyle=boxstyle, facecolor=facecolor, alpha=alpha)

    # Add text box
    ax.text(position[0], position[1], textstr, transform=ax.transAxes,
            fontsize=14, verticalalignment='top', bbox=box_props)

    plt.tight_layout()
    plt.show()
```

Теперь используем эту функцию, чтобы попробовать разные стили блоков. В новой ячейке введите и запустите:

```python
# Try a square box with light green color
plot_with_textbox('square', 'lightgreen', 0.7)

# Try a rounded box with light blue color
plot_with_textbox('round', 'lightblue', 0.5)

# Try a box with extra rounded corners
plot_with_textbox('round4', 'lightyellow', 0.6)

# Try a sawtooth style box
plot_with_textbox('sawtooth', 'lightcoral', 0.4)
```

При запуске этой ячейки вы увидите четыре разных графика, каждый с разным стилем текстового блока.

## Изменение положения текстового блока

Положение текстового блока может быть важным для визуализации. Поместим текстовые блоки в разные углы графика. В новой ячейке введите и запустите:

```python
# Create a figure with a 2x2 grid of subplots
fig, axes = plt.subplots(2, 2, figsize=(12, 10))
axes = axes.flatten()  # Flatten to easily iterate

# Define positions for the four corners
positions = [
    (0.05, 0.95),  # Top left
    (0.95, 0.95),  # Top right
    (0.05, 0.05),  # Bottom left
    (0.95, 0.05)   # Bottom right
]

# Define alignments for each position
alignments = [
    ('top', 'left'),          # Top left
    ('top', 'right'),         # Top right
    ('bottom', 'left'),       # Bottom left
    ('bottom', 'right')       # Bottom right
]

# Corner labels
corner_labels = ['Top Left', 'Top Right', 'Bottom Left', 'Bottom Right']

# Create four plots with text boxes in different corners
for i, ax in enumerate(axes):
    # Plot histogram
    ax.hist(x, bins=50, color='skyblue', edgecolor='black')

    # Set title
    ax.set_title(f'Text Box in {corner_labels[i]}', fontsize=14)

    # Create text box properties
    box_props = dict(boxstyle='round', facecolor='wheat', alpha=0.5)

    # Add text box
    ax.text(positions[i][0], positions[i][1], textstr,
            transform=ax.transAxes, fontsize=12,
            verticalalignment=alignments[i][0],
            horizontalalignment=alignments[i][1],
            bbox=box_props)

plt.tight_layout()
plt.show()
```

Этот код создает сетку из четырех гистограмм 2x2, каждая с текстовым блоком в разных углах.

## Понимание позиционирования текстового блока

Существует несколько ключевых параметров, которые контролируют позиционирование текстового блока:

1. **Координаты позиции**: Координаты `(x, y)` определяют, где будет размещен текстовый блок. При использовании `transform=ax.transAxes` они заданы в координатах осей, где `(0, 0)` - нижний левый угол, а `(1, 1)` - верхний правый угол.

2. **Вертикальное выравнивание**: Параметр `verticalalignment` контролирует, как текст выравнивается вертикально относительно y - координаты:

   - `'top'`: Верхний край текста находится на указанной y - координате.
   - `'center'`: Центр текста находится на указанной y - координате.
   - `'bottom'`: Нижний край текста находится на указанной y - координате.

3. **Горизонтальное выравнивание**: Параметр `horizontalalignment` контролирует, как текст выравнивается горизонтально относительно x - координаты:
   - `'left'`: Левый край текста находится на указанной x - координате.
   - `'center'`: Центр текста находится на указанной x - координате.
   - `'right'`: Правый край текста находится на указанной x - координате.

Эти параметры выравнивания особенно важны при размещении текста в углах. Например, в правом верхнем углу вы бы хотели использовать `horizontalalignment='right'`, чтобы правый край текста выравнивался с правым краем графика.
