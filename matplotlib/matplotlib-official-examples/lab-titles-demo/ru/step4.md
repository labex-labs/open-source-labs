# Продвинутое позиционирование заголовков при работе с подграфиками

На этом этапе вы научитесь продвинутым техникам позиционирования заголовков при работе с макетами подграфиков и объектами осей. Вы также узнаете, как использовать функцию `suptitle()` для добавления общего заголовка к фигуре с несколькими подграфиками.

## Создание фигуры с подграфиками и индивидуальными заголовками

Создадим сетку из 2x2 подграфиков, каждый с собственным заголовком, расположенным по - разному:

```python
# Create a figure with a 2x2 grid of subplots
fig, axes = plt.subplots(2, 2, figsize=(10, 8))

# Flatten the 2D array of axes for easier iteration
axes = axes.flatten()

# Plot data and set titles with different positions for each subplot
for i, ax in enumerate(axes):
    ax.plot(range(10))
    ax.grid(True)

# Top-left subplot: Default centered title
axes[0].set_title('Default (Centered)')

# Top-right subplot: Left-aligned title
axes[1].set_title('Left-Aligned', loc='left')

# Bottom-left subplot: Right-aligned title
axes[2].set_title('Right-Aligned', loc='right')

# Bottom-right subplot: Custom positioned title
axes[3].set_title('Custom Position', y=0.85, loc='center')

# Add spacing between subplots
plt.tight_layout()
plt.show()
```

Запустите ячейку. Вы должны увидеть четыре подграфика, каждый с заголовком, расположенным по - разному.

## Добавление общего заголовка фигуры с помощью suptitle()

При работе с несколькими подграфиками вы, возможно, захотите добавить общий заголовок для всей фигуры. Это можно сделать с помощью функции `suptitle()`:

```python
# Create a figure with a 2x2 grid of subplots
fig, axes = plt.subplots(2, 2, figsize=(10, 8))

# Flatten the 2D array of axes for easier iteration
axes = axes.flatten()

# Plot data on each subplot
for i, ax in enumerate(axes):
    ax.plot(range(10))
    ax.grid(True)
    ax.set_title(f'Subplot {i+1}')

# Add an overall title to the figure
fig.suptitle('Multiple Subplots with an Overall Title', fontsize=16)

# Add spacing between subplots
plt.tight_layout()
# Add top spacing for the suptitle
plt.subplots_adjust(top=0.9)
plt.show()
```

Запустите ячейку. Вы должны увидеть четыре подграфика, каждый с собственным заголовком, и общий заголовок фигуры вверху.

## Комбинирование заголовков осей и заголовков фигуры

Вы можете комбинировать индивидуальные заголовки подграфиков с общим заголовком фигуры:

```python
# Create a figure with a 2x2 grid of subplots
fig, axes = plt.subplots(2, 2, figsize=(10, 8))

# Plot data on each subplot with different title positions
axes[0, 0].plot(range(10))
axes[0, 0].grid(True)
axes[0, 0].set_title('Centered Title', loc='center')

axes[0, 1].plot(range(10))
axes[0, 1].grid(True)
axes[0, 1].set_title('Left-Aligned Title', loc='left')

axes[1, 0].plot(range(10))
axes[1, 0].grid(True)
axes[1, 0].set_title('Right-Aligned Title', loc='right')

axes[1, 1].plot(range(10))
axes[1, 1].grid(True)
axes[1, 1].set_title('Lower Title', y=0.85)

# Add an overall title to the figure
fig.suptitle('Advanced Title Positioning Demo', fontsize=16)

# Add spacing between subplots
plt.tight_layout()
# Add top spacing for the suptitle
plt.subplots_adjust(top=0.9)
plt.show()
```

Запустите ячейку. Вы должны увидеть фигуру с четырьмя подграфиками, каждый с заголовком, расположенным по - разному, и общий заголовок вверху фигуры.

Функция `suptitle()` полезна для добавления основного заголовка, описывающего всю фигуру, в то время как отдельные вызовы `set_title()` для объектов осей добавляют более конкретные заголовки к каждому подграфику.
