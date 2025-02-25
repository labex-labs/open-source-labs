# Задаем пределы и метки графика

Мы зададим пределы и метки графика, чтобы соответствовать требуемому выводу.

```python
for ax in axs:
    ax.set(xlim=(-0.1, 1.1), ylim=(-.8, 3.9), xticks=[], yticks=[])
    ax.set_title(f"usetex={ax.usetex}\n")
```
