# Diagramme in Subfiguren erstellen

Um Daten in den Subfiguren zu plotten, müssen Sie für jede Subfigur ein Subplot mit `subfig.subplots()` erstellen. Anschließend können Sie jede der Diagrammfunktionen in Matplotlib verwenden, um die Diagramme zu erstellen.

```python
ax1 = subfigs[0].subplots()
ax1.plot(np.arange(10), np.random.randn(10))

ax2 = subfigs[1].subplots()
ax2.plot(np.arange(10), np.random.randn(10))
```

Dies erstellt zwei Subfiguren, jede mit einem Diagramm von zufälligen Daten.
