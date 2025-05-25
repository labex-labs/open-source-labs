# 사각형의 모서리 생성

사각형을 사용하여 히스토그램을 그리기 위해 각 사각형의 모서리를 계산해야 합니다. 다음 코드를 추가하십시오:

```python
left = bins[:-1]
right = bins[1:]
bottom = np.zeros(len(left))
top = bottom + n
```
