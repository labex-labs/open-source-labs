# 파이프라인 학습

이제 `fit` 메서드를 사용하여 학습 서브셋에서 파이프라인을 학습합니다. 학습 중 `SelectKBest` 함수는 ANOVA F-값을 기반으로 가장 정보가 풍부한 3 개의 특징을 선택하고, `LinearSVC` 함수는 선택된 특징에 선형 SVM 분류기를 학습합니다.

```python
anova_svm.fit(X_train, y_train)
```
