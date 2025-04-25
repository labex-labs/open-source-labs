# シーケンスに対する回帰を行う

`SequenceKernel`を使って、シーケンスに対する回帰を行うことができます。6 つのシーケンスのデータセットを使い、1 番目、2 番目、4 番目、5 番目のシーケンスを訓練セットとして使って、3 番目と 6 番目のシーケンスに対する予測を行います。

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
