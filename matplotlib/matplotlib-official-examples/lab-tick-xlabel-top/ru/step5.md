# Сохранение и обмен графиком

Последний шаг - сохранить настроенный график, чтобы включить его в отчеты, презентации или поделиться с другими.

## Сохранение графиков в различных форматах

Matplotlib позволяет сохранять графики в различных форматах, включая PNG, JPG, PDF, SVG и другие. Давайте узнаем, как сохранить наш график в разных форматах:

```python
# Create a plot similar to our previous customized one
fig, ax = plt.subplots(figsize=(10, 6))

# Generate data
x = np.linspace(0, 2*np.pi, 100)
y1 = np.sin(x)
y2 = np.cos(x)

# Plot the data
ax.plot(x, y1, linewidth=2, color='blue', label='sin(x)')
ax.plot(x, y2, linewidth=2, color='red', label='cos(x)')

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

# Add title and labels
ax.set_title('Plot with X-Axis Labels at the Top', fontsize=14)
ax.set_xlabel('X-axis at the top')
ax.set_ylabel('Y-axis')

# Add grid and legend
ax.grid(True)
ax.legend()

# Save the figure in different formats
plt.savefig('plot_with_top_xlabels.png', dpi=300, bbox_inches='tight')
plt.savefig('plot_with_top_xlabels.pdf', bbox_inches='tight')
plt.savefig('plot_with_top_xlabels.svg', bbox_inches='tight')

# Show the plot
plt.show()

print("The plot has been saved in PNG, PDF, and SVG formats in the current directory.")
```

При запуске этого кода график будет сохранен в трех различных форматах:

- PNG: Растровый формат изображения, подходящий для веб-страниц и общего использования.
- PDF: Векторный формат, идеальный для публикаций и отчетов.
- SVG: Векторный формат, отлично подходящий для веб-страниц и редактируемых графиков.

Файлы будут сохранены в текущем рабочем каталоге вашего Jupyter-ноутбука.

## Понимание параметров сохранения

Рассмотрим параметры, используемые с `savefig()`:

- `dpi=300`: Устанавливает разрешение (точек на дюйм) для растровых форматов, таких как PNG.
- `bbox_inches='tight'`: Автоматически настраивает границы фигуры так, чтобы включить все элементы без лишнего белого пространства.

## Просмотр сохраненных файлов

Вы можете просмотреть сохраненные файлы, перейдя в файловый браузер в Jupyter:

1. Нажмите на логотип "Jupyter" в левом верхнем углу.
2. В файловом браузере вы должны увидеть сохраненные файлы изображений.
3. Нажмите на любой файл, чтобы просмотреть или скачать его.

## Дополнительные параметры экспорта графиков

Для более точного контроля над сохраненным графиком вы можете настроить размер фигуры, изменить фон или изменить DPI в соответствии с вашими потребностями:

```python
# Control the background color and transparency
fig.patch.set_facecolor('white')  # Set figure background color
fig.patch.set_alpha(0.8)          # Set background transparency

# Save with custom settings
plt.savefig('custom_background_plot.png',
            dpi=400,              # Higher resolution
            facecolor=fig.get_facecolor(),  # Use the figure's background color
            edgecolor='none',     # No edge color
            bbox_inches='tight',  # Tight layout
            pad_inches=0.1)       # Add a small padding

print("A customized plot has been saved with specialized export settings.")
```

Это показывает, как сохранять графики с точным контролем выходного формата и внешнего вида.
