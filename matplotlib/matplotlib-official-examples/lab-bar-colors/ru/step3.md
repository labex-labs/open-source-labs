# Создаем столбчатую диаграмму

Теперь мы можем создать столбчатую диаграмму с использованием данных, определенных на шаге 2. Мы будем использовать метод `bar()` из модуля `pyplot` библиотеки Matplotlib для создания диаграммы. Также мы передадим параметры `label` и `color`, чтобы управлять записями легенды и цветами столбцов соответственно. Следующий код демонстрирует, как создать столбчатую диаграмму:

```python
fig, ax = plt.subplots()
ax.bar(fruits, counts, label=bar_labels, color=bar_colors)
ax.set_ylabel('fruit supply')
ax.set_title('Fruit supply by kind and color')
ax.legend(title='Fruit color')
plt.show()
```
