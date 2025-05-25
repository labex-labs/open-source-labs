# 데이터 마스킹

이 단계에서는 부울 마스크를 사용하여 일부 `z` 값을 마스킹합니다. `np.zeros_like()` 함수를 사용하여 `mask` 배열을 생성한 다음, 일부 값을 `True`로 설정하여 마스킹합니다.

```python
# Mask various z values.
mask = np.zeros_like(z, dtype=bool)
mask[2, 3:5] = True
mask[3:5, 4] = True
mask[7, 2] = True
mask[5, 0] = True
mask[0, 6] = True
z = np.ma.array(z, mask=mask)
```
