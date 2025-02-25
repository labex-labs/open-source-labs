# Настраиваем выравнивание меток делений

Наконец, мы можем использовать методы `set_ha` и `set_va` для настройки горизонтального и вертикального выравнивания меток делений.

```python
ax.axis["left"].major_ticklabels.set_ha("center")
ax.axis["bottom"].major_ticklabels.set_va("top")
```
