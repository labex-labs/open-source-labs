# 로지스틱 회귀

로지스틱 회귀는 로지스틱 함수를 사용하여 가능한 결과의 확률을 추정하는 분류 방법입니다. 이는 일반적으로 이진 분류 작업에 사용됩니다. 로지스틱 회귀는 다중 클래스 분류 문제를 처리하도록 확장될 수도 있습니다.

로지스틱 회귀 모델을 적합해 보겠습니다.

```python
clf = linear_model.LogisticRegression(random_state=0).fit(X, y)
print(clf.coef_)
```

- `random_state` 매개변수를 0 으로 설정한 `LogisticRegression`의 인스턴스를 생성합니다.
- `fit` 메서드를 사용하여 모델을 학습 데이터에 적합시킵니다.
- 로지스틱 회귀 모델의 계수를 출력합니다.
