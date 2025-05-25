# 모델 예측 및 평가

학습된 모델을 사용하여 테스트 하위 집합의 샘플에 대한 숫자 값을 예측합니다. 그런 다음 `sklearn.metrics`의 `metrics.classification_report()` 및 `metrics.ConfusionMatrixDisplay.from_predictions()` 메서드를 사용하여 모델을 평가합니다.

```python
predicted = clf.predict(X_test)

print(
    f"분류기 {clf}에 대한 분류 보고서:\n"
    f"{metrics.classification_report(y_test, predicted)}\n"
)

disp = metrics.ConfusionMatrixDisplay.from_predictions(y_test, predicted)
disp.figure_.suptitle("혼동 행렬")
print(f"혼동 행렬:\n{disp.confusion_matrix}")
```
