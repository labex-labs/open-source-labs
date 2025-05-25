# 데이터 생성

이 단계에서는 합성 이진 데이터와 투영을 생성합니다.

```python
l = 128
proj_operator = build_projection_operator(l, l // 7)
data = generate_synthetic_data()
proj = proj_operator @ data.ravel()[:, np.newaxis]
proj += 0.15 * np.random.randn(*proj.shape)
```
