# 繰り返し

最も不確定な上位 5 つのポイントを選択し、それらのラベルをラベル付きのデータポイントに追加し、30 個のラベル付きのデータポイントが得られるまでモデルを学習するというプロセスを繰り返します。

```python
max_iterations = 3

for i in range(max_iterations):
    if len(unlabeled_indices) == 0:
        print("No unlabeled items left to label.")
        break

    # select top five uncertain points
    pred_entropies = stats.distributions.entropy(lp_model.label_distributions_.T)
    uncertainty_index = np.argsort(pred_entropies)[::-1]
    uncertainty_index = uncertainty_index[np.in1d(uncertainty_index, unlabeled_indices)][:5]

    # add labels to labeled data points
    y_train[uncertainty_index] = y[uncertainty_index]

    # train the model
    lp_model.fit(X, y_train)

    # remove labeled data points from the unlabeled set
    delete_indices = np.array([], dtype=int)
    for index, image_index in enumerate(uncertainty_index):
        (delete_index,) = np.where(unlabeled_indices == image_index)
        delete_indices = np.concatenate((delete_indices, delete_index))
    unlabeled_indices = np.delete(unlabeled_indices, delete_indices)
    n_labeled_points += len(uncertainty_index)
```
