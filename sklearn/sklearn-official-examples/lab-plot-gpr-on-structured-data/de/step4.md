# Führe Klassifizierung auf Sequenzen durch

Wir können unseren `SequenceKernel` verwenden, um Klassifizierung auf Sequenzen durchzuführen. Wir werden einen Datensatz von 6 Sequenzen verwenden und trainieren, ob in der Sequenz 'A's vorhanden sind. Wir werden dann Vorhersagen für weitere 5 Sequenzen machen, wobei die tatsächlichen Werte einfach darauf abzielen, ob in der Sequenz mindestens ein 'A' vorhanden ist. Hierbei machen wir vier richtige Klassifizierungen und verfehlen eine.

```python
X_train = np.array(["AGCT", "CGA", "TAAC", "TCG", "CTTT", "TGCT"])
# ob in der Sequenz 'A's vorhanden sind
Y_train = np.array([True, True, True, False, False, False])

gp = GaussianProcessClassifier(kernel)
gp.fit(X_train, Y_train)

X_test = ["AAA", "ATAG", "CTC", "CT", "C"]
Y_test = [True, True, False, False, False]

plt.figure(figsize=(8, 5))
plt.scatter(
    np.arange(len(X_train)),
    [1.0 if c else -1.0 for c in Y_train],
    s=100,
    marker="o",
    edgecolor="none",
    facecolor=(1, 0.75, 0),
    label="training",
)
plt.scatter(
    len(X_train) + np.arange(len(X_test)),
    [1.0 if c else -1.0 for c in Y_test],
    s=100,
    marker="o",
    edgecolor="none",
    facecolor="r",
    label="truth",
)
plt.scatter(
    len(X_train) + np.arange(len(X_test)),
    [1.0 if c else -1.0 for c in gp.predict(X_test)],
    s=100,
    marker="x",
    facecolor="b",
    linewidth=2,
    label="prediction",
)
plt.xticks(np.arange(len(X_train) + len(X_test)), np.concatenate((X_train, X_test)))
plt.yticks([-1, 1], [False, True])
plt.title("Classification on sequences")
plt.legend()
plt.show()
```
