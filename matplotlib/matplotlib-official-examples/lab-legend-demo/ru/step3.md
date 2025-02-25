# Прикрепить легенды к более сложным графикам

В этом шаге мы прикрепим легенды к более сложным графикам.

```python
# Define data for the chart
fig, axs = plt.subplots(3, 1, layout="constrained")
top_ax, middle_ax, bottom_ax = axs

# Create a bar chart with multiple bars
top_ax.bar([0, 1, 2], [0.2, 0.3, 0.1], width=0.4, label="Bar 1",
           align="center")
top_ax.bar([0.5, 1.5, 2.5], [0.3, 0.2, 0.2], color="red", width=0.4,
           label="Bar 2", align="center")
top_ax.legend()

# Create an error bar chart with multiple errors
middle_ax.errorbar([0, 1, 2], [2, 3, 1], xerr=0.4, fmt="s", label="test 1")
middle_ax.errorbar([0, 1, 2], [3, 2, 4], yerr=0.3, fmt="o", label="test 2")
middle_ax.errorbar([0, 1, 2], [1, 1, 3], xerr=0.4, yerr=0.3, fmt="^",
                   label="test 3")
middle_ax.legend()

# Create a stem chart with a legend
bottom_ax.stem([0.3, 1.5, 2.7], [1, 3.6, 2.7], label="stem test")
bottom_ax.legend()

# Display the chart
plt.show()
```

# Прикрепить легенды к более сложным графикам

В этом шаге мы прикрепим легенды к более сложным графикам.

```python
# Определить данные для графика
fig, axs = plt.subplots(3, 1, layout="constrained")
top_ax, middle_ax, bottom_ax = axs

# Создать столбчатую диаграмму с несколькими столбцами
top_ax.bar([0, 1, 2], [0.2, 0.3, 0.1], width=0.4, label="Столбец 1",
           align="center")
top_ax.bar([0.5, 1.5, 2.5], [0.3, 0.2, 0.2], color="red", width=0.4,
           label="Столбец 2", align="center")
top_ax.legend()

# Создать график с погрешностями с несколькими погрешностями
middle_ax.errorbar([0, 1, 2], [2, 3, 1], xerr=0.4, fmt="s", label="тест 1")
middle_ax.errorbar([0, 1, 2], [3, 2, 4], yerr=0.3, fmt="o", label="тест 2")
middle_ax.errorbar([0, 1, 2], [1, 1, 3], xerr=0.4, yerr=0.3, fmt="^",
                   label="тест 3")
middle_ax.legend()

# Создать стволовую диаграмму с легендой
bottom_ax.stem([0.3, 1.5, 2.7], [1, 3.6, 2.7], label="тест ствола")
bottom_ax.legend()

# Отобразить график
plt.show()
```
