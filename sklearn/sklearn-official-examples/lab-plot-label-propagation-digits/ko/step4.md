# 모델 성능 평가

모델의 성능을 평가하기 위해 분류 보고서와 혼동 행렬을 생성합니다.

```python
predicted_labels = lp_model.transduction_[unlabeled_set]
true_labels = y[unlabeled_set]

print(
    "레이블 확산 모델: %d 레이블 지정된 점 & %d 레이블 미지정 점 (%d 총)"
    % (n_labeled_points, n_total_samples - n_labeled_points, n_total_samples)
)

print(classification_report(true_labels, predicted_labels))

ConfusionMatrixDisplay.from_predictions(
    true_labels, predicted_labels, labels=lp_model.classes_
)
```
