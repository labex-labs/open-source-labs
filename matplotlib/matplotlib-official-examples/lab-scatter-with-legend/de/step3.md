# Automatisches Erstellen der Legende

Wir können auch die Methode `PathCollection.legend_elements` verwenden, um automatisch eine Legende für einen Scatterplot zu erstellen. Diese Methode versucht, eine sinnvolle Anzahl von Legende-Einträgen zu bestimmen, die angezeigt werden sollen, und gibt ein Tupel aus Handles und Labels zurück.

```python
N = 45
x, y = np.random.rand(2, N)
c = np.random.randint(1, 5, size=N)
s = np.random.randint(10, 220, size=N)

fig, ax = plt.subplots()

scatter = ax.scatter(x, y, c=c, s=s)

# erzeuge eine Legende mit den eindeutigen Farben aus dem Scatter
legend1 = ax.legend(*scatter.legend_elements(),
                    loc="lower left", title="Klassen")
ax.add_artist(legend1)

# erzeuge eine Legende mit einem Querschnitt von Größen aus dem Scatter
handles, labels = scatter.legend_elements(prop="sizes", alpha=0.6)
legend2 = ax.legend(handles, labels, loc="upper right", title="Größen")

plt.show()
```
