# 서포트 벡터 머신 (SVM) 분류 모델 학습

```python
param_grid = {
    "C": loguniform(1e3, 1e5),
    "gamma": loguniform(1e-4, 1e-1),
}

clf = RandomizedSearchCV(
    SVC(kernel="rbf", class_weight="balanced"), param_grid, n_iter=10
)
clf = clf.fit(X_train_pca, y_train)
```

변환된 데이터를 사용하여 SVM 분류 모델을 학습합니다. `RandomizedSearchCV()`를 사용하여 SVM 모델에 대한 최적의 하이퍼파라미터를 찾습니다.
