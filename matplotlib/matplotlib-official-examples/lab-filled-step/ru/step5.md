# Настраиваем циклы стилей

Мы настроим циклы стилей для гистограмм с использованием `cycler`. Мы создадим три цикла стилей: один для цвета заливки, один для метки и один для шаблона штриховки.

```python
color_cycle = cycler(facecolor=plt.rcParams['axes.prop_cycle'][:4])
label_cycle = cycler(label=[f'set {n}' for n in range(4)])
hatch_cycle = cycler(hatch=['/', '*', '+', '|'])
```
