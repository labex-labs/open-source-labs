# Tracez les scores de décision pour deux classes

Dans cette étape, nous allons tracer les scores de décision pour deux classes. Nous utiliserons la méthode `decision_function` du classifieur AdaBoost pour obtenir les scores de décision pour chaque échantillon dans l'ensemble de données. Nous tracerons ensuite les histogrammes des scores de décision pour chaque classe.

```python
# Tracez les scores de décision pour deux classes
twoclass_output = bdt.decision_function(X)
plot_range = (twoclass_output.min(), twoclass_output.max())
plt.subplot(122)
for i, n, c in zip(range(2), class_names, plot_colors):
    plt.hist(
        twoclass_output[y == i],
        bins=10,
        range=plot_range,
        facecolor=c,
        label="Class %s" % n,
        alpha=0.5,
        edgecolor="k",
    )
x1, x2, y1, y2 = plt.axis()
plt.axis((x1, x2, y1, y2 * 1.2))
plt.legend(loc="upper right")
plt.ylabel("Samples")
plt.xlabel("Score")
plt.title("Decision Scores")

plt.tight_layout()
plt.subplots_adjust(wspace=0.35)
plt.show()
```
