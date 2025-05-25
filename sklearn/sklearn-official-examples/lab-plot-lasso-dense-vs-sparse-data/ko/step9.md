# 밀집 Lasso 와 희소 Lasso 계수 비교

밀집 Lasso 모델과 희소 Lasso 모델의 계수를 비교하여 동일한 결과를 생성하는지 확인합니다. 계수 간 차이의 유클리드 노름을 계산합니다.

```python
coeff_diff = linalg.norm(sparse_lasso.coef_ - dense_lasso.coef_)
print(f"Distance between coefficients : {coeff_diff:.2e}")
```
