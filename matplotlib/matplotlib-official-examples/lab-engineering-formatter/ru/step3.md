# Создать фигуру и подграфики

Нам нужно создать фигуру и подграфики для отображения данных. В этом практическом занятии мы создадим два подграфика, расположенных рядом.

```python
# Figure width is doubled (2*6.4) to display nicely 2 subplots side by side.
fig, (ax0, ax1) = plt.subplots(nrows=2, figsize=(7, 9.6))
for ax in (ax0, ax1):
    ax.set_xscale('log')
```
