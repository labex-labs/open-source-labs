# Anwenden der Funktion

Jetzt, da wir die Funktionen haben, können wir sie verwenden, um eine Heatmap mit Anmerkungen zu erstellen. Wir erstellen einen neuen Datensatz, geben weitere Argumente an `imshow`, verwenden ein ganzzahliges Format für die Anmerkungen und geben einige Farben an. Wir verstecken auch die Diagonalelemente (die alle 1 sind), indem wir einen `matplotlib.ticker.FuncFormatter` verwenden.

```python
data = np.random.randint(2, 100, size=(7, 7))
y = [f"Book {i}" for i in range(1, 8)]
x = [f"Store {i}" for i in list("ABCDEFG")]

fig, ax = plt.subplots()
im, _ = heatmap(data, y, x, ax=ax, vmin=0, cmap="magma_r", cbarlabel="weekly sold copies")
annotate_heatmap(im, valfmt="{x:d}", size=7, threshold=20, textcolors=("red", "white"))

def func(x, pos):
    return f"{x:.2f}".replace("0.", ".").replace("1.00", "")

annotate_heatmap(im, valfmt=matplotlib.ticker.FuncFormatter(func), size=7)
```
