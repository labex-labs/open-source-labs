# Erstellen eines Stengelplots

Als nächstes erstellen wir einen Stengelplot mit einigen Unterschieden in den Höhen, um auch nahe beieinander liegende Ereignisse zu unterscheiden. Wir fügen Marker auf der Grundlinie hinzu, um die eindimensionale Natur der Zeitlinie visuell zu betonen. Für jedes Ereignis fügen wir eine Textbeschriftung über `~.Axes.annotate` hinzu, die in Punkten von der Spitze der Ereignislinie versetzt ist. Hier ist der Code zum Erstellen eines Stengelplots:

```python
# Wähle einige schöne Höhen
levels = np.tile([-5, 5, -3, 3, -1, 1],
                 int(np.ceil(len(dates)/6)))[:len(dates)]

# Erstelle Figur und zeichne einen Stengelplot mit dem Datum
fig, ax = plt.subplots(figsize=(8.8, 4), layout="constrained")
ax.set(title="Matplotlib release dates")

ax.vlines(dates, 0, levels, color="tab:red")  # Die vertikalen Stengel.
ax.plot(dates, np.zeros_like(dates), "-o",
        color="k", markerfacecolor="w")  # Grundlinie und Marker darauf.

# Beschrifte die Linien
for d, l, r in zip(dates, levels, names):
    ax.annotate(r, xy=(d, l),
                xytext=(-3, np.sign(l)*3), textcoords="offset points",
                horizontalalignment="right",
                verticalalignment="bottom" if l > 0 else "top")
```
