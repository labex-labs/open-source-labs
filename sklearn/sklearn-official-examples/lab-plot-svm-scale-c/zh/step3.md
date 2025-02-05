# L2 惩罚情况

我们可以对 `l2` 惩罚重复类似的实验。在这种情况下，理论表明，为了实现预测一致性，随着样本数量的增加，惩罚参数应保持不变。

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

# 绘制未缩放 C 时的结果
results.plot(x="C", ax=axes[0], logx=True)
axes[0].set_ylabel("CV 分数")
axes[0].set_title("未缩放")

# 绘制缩放 C 后的结果
for train_size_idx, label in enumerate(labels):
    results_scaled = results[[label]].assign(
        C_scaled=Cs * float(n_samples * train_sizes[train_size_idx])
    )
    results_scaled.plot(x="C_scaled", ax=axes[1], logx=True, label=label)
axes[1].set_title("将 C 按 1 / n_samples 缩放")

_ = fig.suptitle("L2 惩罚下缩放 C 的效果")
```
