# Erstellen einer Figur mit Subfiguren

Um eine Figur mit Subfiguren zu erstellen, müssen Sie zunächst ein Figurobjekt mit `plt.figure()` erstellen. Anschließend können Sie Subfiguren mit `fig.subfigures()` erstellen.

```python
fig = plt.figure()
subfigs = fig.subfigures(2, 1)
```

Dies erstellt eine Figur mit zwei Subfiguren, wobei eine über der anderen angeordnet ist.
