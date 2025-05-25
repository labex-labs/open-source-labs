# Realizar Regressão em Sequências

Podemos usar nosso `SequenceKernel` para realizar regressão em sequências. Usaremos um conjunto de dados de 6 sequências e usaremos as 1ª, 2ª, 4ª e 5ª sequências como conjunto de treinamento para fazer previsões nas 3ª e 6ª sequências.

```python
X = np.array(["AGCT", "AGC", "AACT", "TAA", "AAA", "GAACA"])
Y = np.array([1.0, 1.0, 2.0, 2.0, 3.0, 3.0])

training_idx = [0, 1, 3, 4]
gp = GaussianProcessRegressor(kernel=kernel)
gp.fit(X[training_idx], Y[training_idx])

plt.figure(figsize=(8, 5))
plt.bar(np.arange(len(X)), gp.predict(X), color="b", label="predição")
plt.bar(training_idx, Y[training_idx], width=0.2, color="r", alpha=1, label="treinamento")
plt.xticks(np.arange(len(X)), X)
plt.title("Regressão em sequências")
plt.legend()
plt.show()
```
