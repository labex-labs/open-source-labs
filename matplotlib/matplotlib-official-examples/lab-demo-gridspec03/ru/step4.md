# Аннотация осей

В этом шаге мы будем аннотировать оси соответствующими номерами вложенных графиков.

```python
def annotate_axes(fig):
    for i, ax in enumerate(fig.axes):
        ax.text(0.5, 0.5, "ax%d" % (i+1), va="center", ha="center")
        ax.tick_params(labelbottom=False, labelleft=False)

annotate_axes(fig)
```
