# Создание финальной визуализации с несколькими текстовыми элементами

На этом последнем этапе мы объединим все, что узнали, чтобы создать комплексную визуализацию, включающую несколько текстовых элементов с разными стилями. Это продемонстрирует, как текстовые блоки можно использовать для улучшения повествования на основе данных.

## Создание продвинутой визуализации

Создадим более сложный график, который включает как нашу гистограмму, так и некоторые дополнительные визуальные элементы. В новой ячейке введите и запустите следующий код:

```python
# Create a figure with a larger size for our final visualization
fig, ax = plt.subplots(figsize=(12, 8))

# Plot the histogram with more bins and a different color
n, bins, patches = ax.hist(x, bins=75, color='lightblue',
                           edgecolor='darkblue', alpha=0.7)

# Add title and labels with improved styling
ax.set_title('Distribution of Random Data with Statistical Annotations',
             fontsize=18, fontweight='bold', pad=20)
ax.set_xlabel('Value', fontsize=14)
ax.set_ylabel('Frequency', fontsize=14)

# Add grid for better readability
ax.grid(True, linestyle='--', alpha=0.7)

# Mark the mean with a vertical line
ax.axvline(x=mu, color='red', linestyle='-', linewidth=2,
           label=f'Mean: {mu:.2f}')

# Mark one standard deviation range
ax.axvline(x=mu + sigma, color='green', linestyle='--', linewidth=1.5,
           label=f'Mean + 1σ: {mu+sigma:.2f}')
ax.axvline(x=mu - sigma, color='green', linestyle='--', linewidth=1.5,
           label=f'Mean - 1σ: {mu-sigma:.2f}')

# Create a text box with statistics in the top left
stats_box_props = dict(boxstyle='round', facecolor='lightyellow',
                      alpha=0.8, edgecolor='gold', linewidth=2)

stats_text = '\n'.join((
    r'$\mathbf{Statistics:}$',
    r'$\mu=%.2f$ (mean)' % (mu,),
    r'$\mathrm{median}=%.2f$' % (median,),
    r'$\sigma=%.2f$ (std. dev.)' % (sigma,)
))

ax.text(0.05, 0.95, stats_text, transform=ax.transAxes, fontsize=14,
        verticalalignment='top', bbox=stats_box_props)

# Add an informational text box in the top right
info_box_props = dict(boxstyle='round4', facecolor='lightcyan',
                     alpha=0.8, edgecolor='deepskyblue', linewidth=2)

info_text = '\n'.join((
    r'$\mathbf{About\ Normal\ Distributions:}$',
    r'$\bullet\ 68\%\ of\ data\ within\ 1\sigma$',
    r'$\bullet\ 95\%\ of\ data\ within\ 2\sigma$',
    r'$\bullet\ 99.7\%\ of\ data\ within\ 3\sigma$'
))

ax.text(0.95, 0.95, info_text, transform=ax.transAxes, fontsize=14,
        verticalalignment='top', horizontalalignment='right',
        bbox=info_box_props)

# Add a legend
ax.legend(fontsize=12)

# Tighten the layout and show the plot
plt.tight_layout()
plt.show()
```

При запуске этой ячейки вы увидите комплексную визуализацию с:

- Гистограммой данных с улучшенным стилем.
- Вертикальными линиями, отмечающими среднее значение и диапазон в одну стандартную ошибку.
- Текстовым блоком со статистикой в левом верхнем углу.
- Информационным текстовым блоком о нормальных распределениях в правом верхнем углу.
- Легендой, объясняющей вертикальные линии.

## Понимание продвинутых элементов

Рассмотрим некоторые из новых элементов, которые мы добавили:

1. **Вертикальные линии с помощью `axvline()`**:

   - Эти линии отмечают важные статистические показатели прямо на графике.
   - Параметр `label` позволяет включить эти линии в легенду.

2. **Несколько текстовых блоков с разными стилями**:

   - Каждый текстовый блок служит разной цели и имеет свой уникальный стиль.
   - Блок со статистикой показывает вычисленные значения из наших данных.
   - Информационный блок предоставляет контекст о нормальных распределениях.

3. **Улучшенный формат**:

   - Форматирование LaTeX используется для создания жирного текста с помощью `\mathbf{}`.
   - Маркеры списка создаются с помощью `\bullet`.
   - Интервал между строками контролируется с помощью `\ ` (обратный слеш, за которым следует пробел).

4. **Сетка и легенда**:
   - Сетка помогает зрителям более точно читать значения с графика.
   - Легенда объясняет смысл цветных линий.

## Финальные замечания о размещении текстовых блоков

При размещении нескольких текстовых элементов в визуализации учитывайте:

1. **Визуальную иерархию**: Самая важная информация должна быть наиболее заметной.
2. **Позиционирование**: Размещайте связанную информацию рядом с соответствующими частями визуализации.
3. **Контраст**: Убедитесь, что текст хорошо читается на фоне его фона.
4. **Согласованность**: Используйте согласованный стиль для однотипной информации.
5. **Загромождение**: Избегайте перегрузки визуализации слишком большим количеством текстовых элементов.

Разумно размещая и стилизуя текстовые блоки, вы можете создать визуализации, которые будут как информативными, так и визуально привлекательными, помогающими зрителям понять ключевые выводы из ваших данных.
