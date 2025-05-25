# 시퀀스에 대한 회귀 수행

`SequenceKernel`을 사용하여 시퀀스에 대한 회귀를 수행할 수 있습니다. 6 개의 시퀀스 데이터 세트를 사용하고 1, 2, 4, 5 번째 시퀀스를 학습 세트로 사용하여 3 번째와 6 번째 시퀀스에 대한 예측을 수행합니다.

```python
X = np.array(["AGCT", "AGC", "AACT", "TAA", "AAA", "GAACA"])
Y = np.array([1.0, 1.0, 2.0, 2.0, 3.0, 3.0])

training_idx = [0, 1, 3, 4]
gp = GaussianProcessRegressor(kernel=kernel)
gp.fit(X[training_idx], Y[training_idx])

plt.figure(figsize=(8, 5))
plt.bar(np.arange(len(X)), gp.predict(X), color="b", label="예측")
plt.bar(training_idx, Y[training_idx], width=0.2, color="r", alpha=1, label="학습")
plt.xticks(np.arange(len(X)), X)
plt.title("시퀀스에 대한 회귀")
plt.legend()
plt.show()
```
