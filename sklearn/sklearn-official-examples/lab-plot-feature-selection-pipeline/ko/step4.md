# 파이프라인 평가

이제 `predict` 메서드를 사용하여 테스트 서브셋에서 파이프라인을 평가합니다. 파이프라인은 ANOVA F-값을 기반으로 가장 정보가 풍부한 3 개의 특징을 선택하고, `LinearSVC` 함수는 선택된 특징에 대한 예측을 수행합니다.

```python
from sklearn.metrics import classification_report

y_pred = anova_svm.predict(X_test)
print(classification_report(y_test, y_pred))
```
