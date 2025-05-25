# 밀집 데이터에 Lasso 적용

Scikit-learn 의 `fit` 함수를 사용하여 밀집 데이터에 Lasso 회귀 모델을 적용합니다. 또한, 적용 시간을 측정하고 각 Lasso 모델의 시간을 출력합니다.

```python
t0 = time()
sparse_lasso.fit(X_sp, y)
print(f"Sparse Lasso done in {(time() - t0):.3f}s")

t0 = time()
dense_lasso.fit(X, y)
print(f"Dense Lasso done in {(time() - t0):.3f}s")
```
