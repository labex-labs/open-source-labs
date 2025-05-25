# 모델 성능 평가

```python
y_pred = clf.predict(X_test_pca)
print(classification_report(y_test, y_pred, target_names=target_names))
ConfusionMatrixDisplay.from_estimator(
    clf, X_test_pca, y_test, display_labels=target_names, xticks_rotation="vertical"
)
```

테스트 데이터를 사용하여 대상 값을 예측하고 `classification_report()` 함수를 사용하여 모델 성능을 평가합니다. 또한 `ConfusionMatrixDisplay()` 함수를 사용하여 혼동 행렬을 플롯합니다.
