# Definieren eines Beispiel-Diagramms

Wir definieren eine Funktion, die ein einfaches Liniendiagramm mit x- und y-Beschriftungen und einem Titel erstellt.

```python
def example_plot(ax):
    ax.plot([1, 2])
    ax.set_xlabel('x-label', fontsize=12)
    ax.set_ylabel('y-label', fontsize=12)
    ax.set_title('Title', fontsize=14)
```
