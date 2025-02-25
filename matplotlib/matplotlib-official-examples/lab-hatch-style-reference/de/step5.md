# Erstellen der zweiten Gruppe von Schraffierungsmustern

Wir werden die zweite Gruppe von Schraffierungsmustern indem wir jedes Muster zweimal wiederholen, um die Dichte zu erhöhen. Wir werden die folgende Liste verwenden:

```python
hatches = ['//', '\\\\', '||', '--', '++', 'xx', 'oo', 'OO', '..', '**']
```

Wir werden die gleiche Schleife wie zuvor verwenden, um die Rechtecke zu erstellen.

```python
for ax, h in zip(axs.flat, hatches):
    hatches_plot(ax, h)
```
