# 마스크된 배열 생성

이 단계에서는 마스크된 배열을 생성하고 데이터를 마스크에 적용합니다.

```python
# create masked array
data = (1, 2, 3, 4, 5, 6, 7, 8)
mask = (1, 0, 1, 0, 0, 0, 1, 0)
xsecs = secs * np.ma.MaskedArray(data, mask, float)
```
