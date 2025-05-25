# 희소 데이터 생성

다음으로, Lasso 회귀에 사용할 희소 데이터를 생성합니다. 이전 단계에서 밀집 데이터를 복사하고, 값이 2.5 미만인 모든 값을 0 으로 바꿉니다. 또한, 희소 데이터를 Scipy 의 Compressed Sparse Column 형식으로 변환합니다.

```python
Xs = X.copy()
Xs[Xs < 2.5] = 0.0
Xs_sp = sparse.coo_matrix(Xs)
Xs_sp = Xs_sp.tocsc()
```
