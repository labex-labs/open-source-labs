# Создание меню

Теперь мы можем создать меню. Мы создаем новую фигуру и настраиваем левый отступ. Затем мы создаем список элементов меню и добавляем их в меню. Мы также определяем функцию обратного вызова для каждого элемента, которая будет выводить выбранный элемент.

```python
fig = plt.figure()
fig.subplots_adjust(left=0.3)
props = ItemProperties(labelcolor='black', bgcolor='yellow',
                       fontsize=15, alpha=0.2)
hoverprops = ItemProperties(labelcolor='white', bgcolor='blue',
                            fontsize=15, alpha=0.2)

menuitems = []
for label in ('open', 'close','save','save as', 'quit'):
    def on_select(item):
        print('you selected %s' % item.labelstr)
    item = MenuItem(fig, label, props=props, hoverprops=hoverprops,
                    on_select=on_select)
    menuitems.append(item)

menu = Menu(fig, menuitems)
plt.show()
```
