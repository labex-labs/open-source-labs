# Включаем или отключаем отображение различных элементов

Мы можем включать или отключать отображение различных элементов ящика с усами, используя различные параметры в функции `bxp()`. В этом примере мы демонстрируем, как показать или скрыть среднее значение, коробку, "крышки", зазоры и выбросы.

```python
# Toggle the display of different elements
plt.bxp(stats, showmeans=True, showbox=False, showcaps=False, shownotches=True, showfliers=False)
plt.show()
```
