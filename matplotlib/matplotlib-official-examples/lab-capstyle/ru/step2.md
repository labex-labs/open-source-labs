# Создать график

Далее мы создадим простой график, чтобы продемонстрировать разные варианты `CapStyle`.

```python
fig, ax = plt.subplots()

# Plotting the line with different CapStyle options
for i, cap_style in enumerate(CapStyle):
    ax.plot([0, 1], [i, i], label=str(cap_style), linewidth=10, solid_capstyle=cap_style)

# Adding legend and title
ax.legend(title='CapStyle')
ax.set_title('CapStyle Demo')
```
