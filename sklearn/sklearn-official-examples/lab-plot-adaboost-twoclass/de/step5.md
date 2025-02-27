# Die Entscheidungs-Scores für die Zwei-Klassen-klassifizierung plotten

In diesem Schritt werden wir die Entscheidungs-Scores für die Zwei-Klassen-klassifizierung plotten. Wir verwenden die Methode `decision_function` des AdaBoost-Klassifizierers, um die Entscheidungs-Scores für jede Probe im Datensatz zu erhalten. Anschließend plotten wir die Histogramme der Entscheidungs-Scores für jede Klasse.

```python
# Plot the two-class decision scores
twoclass_output = bdt.decision_function(X)
plot_range = (twoclass_output.min(), twoclass_output.max())
plt.subplot(122)
for i, n, c in zip(range(2), class_names, plot_colors):
    plt.hist(
        twoclass_output[y == i],
        bins=10,
        range=plot_range,
        facecolor=c,
        label="Klasse %s" % n,
        alpha=0.5,
        edgecolor="k",
    )
x1, x2, y1, y2 = plt.axis()
plt.axis((x1, x2, y1, y2 * 1.2))
plt.legend(loc="upper right")
plt.ylabel("Samples")
plt.xlabel("Score")
plt.title("Entscheidungs-Scores")

plt.tight_layout()
plt.subplots_adjust(wspace=0.35)
plt.show()
```
