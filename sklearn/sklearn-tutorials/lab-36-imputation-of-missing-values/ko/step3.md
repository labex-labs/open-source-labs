# IterativeImputer 를 이용한 다변량 특징 임퓨테이션

`IterativeImputer` 클래스는 누락된 값을 임퓨테이션하는 더욱 고급적인 방법입니다. 누락된 값이 있는 각 특징을 다른 특징의 함수로 모델링하고, 그 추정값을 임퓨테이션에 사용합니다. 반복적으로 특징 간의 관계를 학습하고, 이러한 관계를 기반으로 누락된 값을 임퓨테이션합니다.

```python
imp = IterativeImputer()
X = [[1, 2], [3, 6], [4, 8], [np.nan, 3], [7, np.nan]]
imp.fit(X)
X_test = [[np.nan, 2], [6, np.nan], [np.nan, 6]]
imputed_X_test = imp.transform(X_test)
```
