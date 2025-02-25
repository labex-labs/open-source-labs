# Das Balkendiagramm erstellen

Jetzt sind wir bereit, unser Balkendiagramm zu erstellen. Wir beginnen, indem wir einige Variablen definieren, die uns helfen, die Breite der Balken und ihre Position auf der x-Achse festzulegen.

```python
dim = len(data[0])
w = 0.75
dimw = w / dim
```

Als nächstes werden wir mithilfe der `subplots()`-Methode eine Figur und ein Achsenobjekt erstellen. Dann werden wir in einer for-Schleife durch jeden Wert in unserem Datensatz iterieren und für jeden einen Balken erstellen.

```python
fig, ax = plt.subplots()
x = np.arange(len(data))
for i in range(len(data[0])):
    y = [d[i] for d in data]
    b = ax.bar(x + i * dimw, y, dimw, bottom=0.001)
```

Wir legen den Parameter `bottom` auf `0.001` fest, um zu vermeiden, dass es Balken mit einer Höhe von 0 gibt, was mit einer logarithmischen Skala nicht kompatibel ist.
