# 데이터 전처리

SGD 를 적용하기 전에 데이터를 전처리하는 것이 종종 유용합니다. 이 경우 scikit-learn 의 StandardScaler 를 사용하여 특징을 표준화합니다.

```python
scaler = StandardScaler()
X = scaler.fit_transform(X)
```
