# 하이퍼파라미터 및 평가 지표 정의

이 단계에서는 `DecisionTreeClassifier` 모델의 하이퍼파라미터와 사용할 평가 지표를 정의합니다. AUC (곡선 아래 면적) 및 정확도 지표를 사용할 것입니다.

```python
scoring = {"AUC": "roc_auc", "Accuracy": make_scorer(accuracy_score)}
```
