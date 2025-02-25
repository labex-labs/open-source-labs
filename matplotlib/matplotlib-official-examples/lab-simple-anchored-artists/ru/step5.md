# Добавьте шкалу размеров

Нарисуйте горизонтальную шкалу длиной 0,1 в координатах данных, с фиксированной подписью снизу.

```python
asb = AnchoredSizeBar(ax.transData,
                      0.1,
                      r"1$^{\prime}$",
                      loc='lower center',
                      pad=0.1, borderpad=0.5, sep=5,
                      frameon=False)
ax.add_artist(asb)
```
