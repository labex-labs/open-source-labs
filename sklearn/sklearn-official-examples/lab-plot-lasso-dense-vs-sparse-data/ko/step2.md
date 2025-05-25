# 밀집 데이터 생성

다음으로 Lasso 회귀에 사용할 밀집 데이터를 생성합니다. Scikit-learn 의 `make_regression` 함수를 사용하여 200 개의 샘플과 5000 개의 특징을 가진 데이터를 생성합니다.

```python
X, y = make_regression(n_samples=200, n_features=5000, random_state=0)
```
