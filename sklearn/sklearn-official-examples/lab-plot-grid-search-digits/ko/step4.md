# 모델 학습 및 예측 수행

모델을 학습하고 평가 데이터 세트에 대한 예측을 수행합니다.

```python
grid_search.fit(X_train, y_train)

# 사용자 정의 전략으로 그리드 검색에서 선택된 파라미터는 다음과 같습니다:
grid_search.best_params_

# 마지막으로, 미세 조정된 모델을 남겨진 평가 데이터 세트에서 평가합니다.
# `grid_search` 객체는 사용자 정의 재학습 전략으로 선택된 파라미터를 사용하여 **전체 학습 데이터 세트에서 자동으로 재학습되었습니다**.
y_pred = grid_search.predict(X_test)
print(classification_report(y_test, y_pred))
```
