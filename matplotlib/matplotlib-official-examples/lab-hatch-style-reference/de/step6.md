# Erstellen der dritten Gruppe von Schraffierungsmustern

Wir werden die dritte Gruppe von Schraffierungsmustern indem wir zwei Muster kombinieren, um ein neues zu erstellen. Wir werden die folgende Liste verwenden:

```python
hatches = ['/o', '\\|', '|*', '-\\', '+o', 'x*', 'o-', 'O|', 'O.', '*-']
```

Wir werden die gleiche Schleife wie zuvor verwenden, um die Rechtecke zu erstellen.

```python
for ax, h in zip(axs.flat, hatches):
    hatches_plot(ax, h)
```
