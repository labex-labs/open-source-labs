# L1 ペナルティの場合

L1 の場合、理論上、正しい非ゼロパラメータのセットとその符号を見つけるという点で、モデルの整合性は `C` をスケーリングすることで達成できます。この効果を、少数の特徴のみがモデルにとって情報的で有用であるという意味で疎な合成データセットを使って示します。

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

# plot results without scaling C
results.plot(x="C", ax=axes[0], logx=True)
axes[0].set_ylabel("CV score")
axes[0].set_title("No scaling")

# plot results by scaling C
for train_size_idx, label in enumerate(labels):
    results_scaled = results[[label]].assign(
        C_scaled=Cs * float(n_samples * train_sizes[train_size_idx])
    )
    results_scaled.plot(x="C_scaled", ax=axes[1], logx=True, label=label)
axes[1].set_title("Scaling C by 1 / n_samples")

_ = fig.suptitle("Effect of scaling C with L1 penalty")
```
