# Определяем параметры гистограммы

Следующим шагом является определение параметров гистограммы. Мы определим позиции по оси x для групп, ширину столбцов и метки для делений по оси x.

```python
ind = np.arange(N)    # the x locations for the groups
width = 0.35         # the width of the bars
ax.set_xticks(ind + width / 2, labels=['G1', 'G2', 'G3', 'G4', 'G5'])
```
