# L1 惩罚情况

在 L1 惩罚的情况下，理论表明，通过缩放 `C`，在找到正确的非零参数集及其符号方面，可以实现模型一致性。我们使用一个稀疏的合成数据集来演示这种效果，这意味着只有少数特征对模型来说是有信息价值且有用的。

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

_ = fig.suptitle("L1 惩罚下缩放 C 的效果")
```
