# 이미지를 부동소수점으로 변환 및 형상 변경

이미지를 부동소수점으로 변환하고 K-평균 알고리즘에서 처리할 수 있도록 2 차원 NumPy 배열로 형상을 변경합니다.

```python
# 기본 8 비트 정수 코드 대신 부동소수점으로 변환합니다.
china = np.array(china, dtype=np.float64) / 255

# 이미지의 차원을 가져옵니다.
w, h, d = original_shape = tuple(china.shape)
assert d == 3

# 이미지를 2 차원 NumPy 배열로 형상을 변경합니다.
image_array = np.reshape(china, (w * h, d))
```
