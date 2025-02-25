# Создание стандартного violin plot

Далее мы создадим стандартный violin plot с использованием функции `violinplot` Matplotlib. Это будет служить базовой линией для сравнения, когда мы будем настраивать график в последующих шагах.

```python
# create default violin plot
fig, ax1 = plt.subplots()
ax1.set_title('Default Violin Plot')
ax1.set_ylabel('Observed Values')
ax1.violinplot(data)
```
