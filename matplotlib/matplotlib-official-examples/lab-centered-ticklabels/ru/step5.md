# Выровнять метки вторичных делений на шкале

Наконец, нам нужно выровнять метки вторичных делений на шкале посередине между основными делениями. Мы можем сделать это с помощью функции `get_xticklabels()` и настройкой параметра `minor` на `True`, чтобы получить метки вторичных делений. Затем мы можем пройти по меткам в цикле и установить горизонтальное выравнивание в `'center'`.

```python
# Align the minor tick label
for label in ax.get_xticklabels(minor=True):
    label.set_horizontalalignment('center')
imid = len(r) // 2
ax.set_xlabel(str(r.date[imid].item().year))
```
