# Метка столбчатых диаграмм с использованием строки формата `{}`

В этом шаге мы покажем, как использовать строку формата `{}` для форматирования меток на столбчатых диаграммах. Будем использовать некоторые данные о продажах желато по вкусам.

```python
fruit_names = ['Coffee', 'Salted Caramel', 'Pistachio']
fruit_counts = [4000, 2000, 7000]

fig, ax = plt.subplots()
bar_container = ax.bar(fruit_names, fruit_counts)
ax.set(ylabel='pints sold', title='Gelato sales by flavor', ylim=(0, 8000))
ax.bar_label(bar_container, fmt='{:,.0f}')
```
