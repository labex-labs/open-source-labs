# Darstellung der partiellen Abhängigkeit beider Modelle zusammen

In diesem Schritt werden wir die partiellen Abhängigkeitskurven beider Modelle in einem gemeinsamen Plot darstellen.

```python
fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(10, 10))
tree_disp.plot(ax=ax1)
ax1.set_title("Decision Tree")
mlp_disp.plot(ax=ax2, line_kw={"color": "red"})
ax2.set_title("Multi-layer Perceptron")
```

Eine andere Möglichkeit, die Kurven zu vergleichen, ist, sie übereinander zu plotten. Hier erstellen wir eine Figur mit einer Zeile und zwei Spalten. Die Achsen werden als Liste an die `PartialDependenceDisplay.plot`-Funktion übergeben, die die partiellen Abhängigkeitskurven jedes Modells auf den gleichen Achsen plotten wird. Die Länge der Achsenliste muss der Anzahl der gezeichneten Plots entsprechen.

```python
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(10, 6))
tree_disp.plot(ax=[ax1, ax2], line_kw={"label": "Decision Tree"})
mlp_disp.plot(
    ax=[ax1, ax2], line_kw={"label": "Multi-layer Perceptron", "color": "red"}
)
ax1.legend()
ax2.legend()
```

`tree_disp.axes_` ist ein numpy-Array, das die Achsen enthält, die zur Darstellung der partiellen Abhängigkeitsplots verwendet werden. Dies kann an `mlp_disp` übergeben werden, um die gleiche Wirkung zu erzielen, die Plots übereinander zu zeichnen. Darüber hinaus speichert `mlp_disp.figure_` die Figur, was es ermöglicht, die Größe der Figur nach dem Aufruf von `plot` anzupassen. In diesem Fall hat `tree_disp.axes_` zwei Dimensionen, daher wird `plot` nur die y-Beschriftung und die y-Ticks auf dem linken Plot anzeigen.

```python
tree_disp.plot(line_kw={"label": "Decision Tree"})
mlp_disp.plot(
    line_kw={"label": "Multi-layer Perceptron", "color": "red"}, ax=tree_disp.axes_
)
tree_disp.figure_.set_size_inches(10, 6)
tree_disp.axes_[0, 0].legend()
tree_disp.axes_[0, 1].legend()
plt.show()
```
