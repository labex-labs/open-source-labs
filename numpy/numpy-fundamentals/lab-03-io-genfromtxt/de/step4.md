# Auswahl von Spalten

Das Argument `usecols` wird verwendet, um zu wählen, welche Spalten importiert werden sollen. Es akzeptiert eine einzelne Ganzzahl oder eine Sequenz von Ganzzahlen, die den Indizes der zu importierenden Spalten entsprechen.

```python
np.genfromtxt(StringIO(data), usecols=(0, -1))
```
