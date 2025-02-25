# Erstellen der ersten Gruppe von Schraffierungsmustern

Wir werden die erste Gruppe von Schraffierungsmustern mithilfe der folgenden Liste erstellen:

```python
hatches = ['/', '\\', '|', '-', '+', 'x', 'o', 'O', '.', '*']
```

Anschließend werden wir in einer Schleife ein Rechteck mit jedem Schraffierungsmuster erstellen und es zu einem Teilplot hinzufügen.

```python
for ax, h in zip(axs.flat, hatches):
    hatches_plot(ax, h)
```
