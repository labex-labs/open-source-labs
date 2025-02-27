# Führe Regression auf Sequenzen durch

Wir können unseren `SequenceKernel` verwenden, um Regression auf Sequenzen durchzuführen. Wir werden einen Datensatz von 6 Sequenzen verwenden und die 1., 2., 4. und 5. Sequenz als Trainingsmenge verwenden, um Vorhersagen für die 3. und 6. Sequenz zu machen.

```python
X = np.array(["AGCT", "AGC", "AACT", "TAA", "AAA", "GAACA"])
Y = np.array([1.0, 1.0, 2.0, 2.0, 3.0, 3.0])

training_idx = [0, 1, 3, 4]
gp = GaussianProcessRegressor(kernel=kernel)
gp.fit(X[training_idx], Y[training_idx])

plt.figure(figsize=(8, 5))
plt.bar(np.arange(len(X)), gp.predict(X), color="b", label="prediction")
plt.bar(training_idx, Y[training_idx], width=0.2, color="r", alpha=1, label="training")
plt.xticks(np.arange(len(X)), X)
plt.title("Regression on sequences")
plt.legend()
plt.show()
```
