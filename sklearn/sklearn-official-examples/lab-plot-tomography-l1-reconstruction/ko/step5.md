# L1 페널티를 사용한 이미지 재구성

이 단계에서는 L1(라쏘) 페널티를 사용하여 이미지를 재구성합니다.

```python
rgr_lasso = Lasso(alpha=0.001)
rgr_lasso.fit(proj_operator, proj.ravel())
rec_l1 = rgr_lasso.coef_.reshape(l, l)
```
