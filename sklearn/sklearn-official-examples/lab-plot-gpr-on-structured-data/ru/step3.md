# Выполнение регрессии на последовательностях

Мы можем использовать наш `SequenceKernel` для выполнения регрессии на последовательностях. Мы будем использовать датасет из 6 последовательностей и использовать 1-ю, 2-ю, 4-ю и 5-ю последовательности в качестве обучающего набора для предсказания на 3-ю и 6-ю последовательности.

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
