# L2 페널티를 사용한 이미지 재구성

이 단계에서는 L2(릿지) 페널티를 사용하여 이미지를 재구성합니다.

```python
rgr_ridge = Ridge(alpha=0.2)
rgr_ridge.fit(proj_operator, proj.ravel())
rec_l2 = rgr_ridge.coef_.reshape(l, l)
```
