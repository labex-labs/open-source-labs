# 반복

가장 불확실한 상위 5 개 포인트를 선택하고, 이들의 레이블을 레이블된 데이터 포인트에 추가한 후 모델을 학습하는 과정을 레이블된 데이터 포인트가 30 개가 될 때까지 반복합니다.

```python
max_iterations = 3

for i in range(max_iterations):
    if len(unlabeled_indices) == 0:
        print("레이블되지 않은 항목이 더 이상 없습니다.")
        break

    # 상위 5 개의 불확실한 포인트 선택
    pred_entropies = stats.distributions.entropy(lp_model.label_distributions_.T)
    uncertainty_index = np.argsort(pred_entropies)[::-1]
    uncertainty_index = uncertainty_index[np.in1d(uncertainty_index, unlabeled_indices)][:5]

    # 레이블을 레이블된 데이터 포인트에 추가
    y_train[uncertainty_index] = y[uncertainty_index]

    # 모델 학습
    lp_model.fit(X, y_train)

    # 레이블된 데이터 포인트를 레이블되지 않은 집합에서 제거
    delete_indices = np.array([], dtype=int)
    for index, image_index in enumerate(uncertainty_index):
        (delete_index,) = np.where(unlabeled_indices == image_index)
        delete_indices = np.concatenate((delete_indices, delete_index))
    unlabeled_indices = np.delete(unlabeled_indices, delete_indices)
    n_labeled_points += len(uncertainty_index)
```
