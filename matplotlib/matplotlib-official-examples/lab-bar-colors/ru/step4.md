# Настраиваем диаграмму

Мы можем дополнительно настроить диаграмму, добавив подписи осей и заголовок. Также мы можем изменить цвет подписей осей и заголовка легенды. Следующий код демонстрирует, как настроить диаграмму:

```python
fig, ax = plt.subplots()
ax.bar(fruits, counts, label=bar_labels, color=bar_colors)
ax.set_ylabel('fruit supply', color='blue')
ax.set_xlabel('fruit names', color='blue')
ax.set_title('Fruit supply by kind and color', color='purple')
ax.legend(title='Fruit color', title_color='red', labelcolor='green')
plt.show()
```
