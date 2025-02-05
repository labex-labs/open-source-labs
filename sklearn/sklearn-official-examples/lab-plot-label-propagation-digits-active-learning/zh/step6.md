# 重复操作

我们将重复选择最不确定的前五个点、将它们的标签添加到有标签的数据点中以及训练模型的过程，直到我们有30个有标签的数据点。

```python
max_iterations = 3

for i in range(max_iterations):
    if len(unlabeled_indices) == 0:
        print("No unlabeled items left to label.")
        break

    # 选择前五个不确定的点
    pred_entropies = stats.distributions.entropy(lp_model.label_distributions_.T)
    uncertainty_index = np.argsort(pred_entropies)[::-1]
    uncertainty_index = uncertainty_index[np.in1d(uncertainty_index, unlabeled_indices)][:5]

    # 将标签添加到有标签的数据点中
    y_train[uncertainty_index] = y[uncertainty_index]

    # 训练模型
    lp_model.fit(X, y_train)

    # 从未标记集中移除已标记的数据点
    delete_indices = np.array([], dtype=int)
    for index, image_index in enumerate(uncertainty_index):
        (delete_index,) = np.where(unlabeled_indices == image_index)
        delete_indices = np.concatenate((delete_indices, delete_index))
    unlabeled_indices = np.delete(unlabeled_indices, delete_indices)
    n_labeled_points += len(uncertainty_index)
```
