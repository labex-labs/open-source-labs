# L1 페널티 케이스

L1 케이스에서 이론적으로는 모델 일관성 (즉, 올바른 0 이 아닌 매개변수 집합과 그 부호를 찾는 것) 은 `C`를 조정하여 달성할 수 있습니다. 이 효과는 소수의 특징만이 모델에 정보가 되고 유용한 희소한 합성 데이터셋을 사용하여 보여줍니다.

```python
model_l1 = LinearSVC(penalty="l1", loss="squared_hinge", dual=False, tol=1e-3)

Cs = np.logspace(-2.3, -1.3, 10)
train_sizes = np.linspace(0.3, 0.7, 3)
labels = [f"fraction: {train_size}" for train_size in train_sizes]

results = {"C": Cs}
for label, train_size in zip(labels, train_sizes):
    cv = ShuffleSplit(train_size=train_size, test_size=0.3, n_splits=50, random_state=1)
    train_scores, test_scores = validation_curve(
        model_l1, X, y, param_name="C", param_range=Cs, cv=cv
    )
    results[label] = test_scores.mean(axis=1)
results = pd.DataFrame(results)

fig, axes = plt.subplots(nrows=1, ncols=2, sharey=True, figsize=(12, 6))

# C 를 조정하지 않은 결과 플롯
results.plot(x="C", ax=axes[0], logx=True)
axes[0].set_ylabel("CV 점수")
axes[0].set_title("조정 없음")

# C 를 조정한 결과 플롯
for train_size_idx, label in enumerate(labels):
    results_scaled = results[[label]].assign(
        C_scaled=Cs * float(n_samples * train_sizes[train_size_idx])
    )
    results_scaled.plot(x="C_scaled", ax=axes[1], logx=True, label=label)
axes[1].set_title("C 를 n_samples 로 조정")

_ = fig.suptitle("L1 페널티로 C 조정 효과")
```
