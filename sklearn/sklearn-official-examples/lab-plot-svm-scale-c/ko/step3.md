# L2 페널티 케이스

`l2` 페널티로 유사한 실험을 반복할 수 있습니다. 이 경우 이론적으로 예측 일관성을 달성하기 위해 페널티 매개변수는 샘플 수가 증가함에 따라 일정하게 유지되어야 합니다.

```python
model_l2 = LinearSVC(penalty="l2", loss="squared_hinge", dual=True)
Cs = np.logspace(-4.5, -2, 10)

labels = [f"fraction: {train_size}" for train_size in train_sizes]
results = {"C": Cs}
for label, train_size in zip(labels, train_sizes):
    cv = ShuffleSplit(train_size=train_size, test_size=0.3, n_splits=50, random_state=1)
    train_scores, test_scores = validation_curve(
        model_l2, X, y, param_name="C", param_range=Cs, cv=cv
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

_ = fig.suptitle("L2 페널티로 C 조정 효과")
```
