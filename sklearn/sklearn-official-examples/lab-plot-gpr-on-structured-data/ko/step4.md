# 시퀀스 분류 수행

`SequenceKernel`을 사용하여 시퀀스에 대한 분류를 수행할 수 있습니다. 6 개의 시퀀스 데이터 세트를 사용하고 시퀀스에 'A'가 있는지 여부를 기반으로 학습합니다. 그런 다음 다른 5 개의 시퀀스에 대한 예측을 수행하며, 실제 값은 시퀀스에 적어도 하나의 'A'가 있는지 여부입니다. 여기서 네 개의 분류가 정확하고 하나의 분류가 실패합니다.

```python
X_train = np.array(["AGCT", "CGA", "TAAC", "TCG", "CTTT", "TGCT"])
# 시퀀스에 'A'가 있는지 여부
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
    label="학습",
)
plt.scatter(
    len(X_train) + np.arange(len(X_test)),
    [1.0 if c else -1.0 for c in Y_test],
    s=100,
    marker="o",
    edgecolor="none",
    facecolor="r",
    label="실제값",
)
plt.scatter(
    len(X_train) + np.arange(len(X_test)),
    [1.0 if c else -1.0 for c in gp.predict(X_test)],
    s=100,
    marker="x",
    facecolor="b",
    linewidth=2,
    label="예측",
)
plt.xticks(np.arange(len(X_train) + len(X_test)), np.concatenate((X_train, X_test)))
plt.yticks([-1, 1], [False, True])
plt.title("시퀀스 분류")
plt.legend()
plt.show()
```
