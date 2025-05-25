# 좌표 준비

다음으로, 복셀 플롯에 대한 좌표를 준비합니다. NumPy 의 `indices` 함수를 사용하여 8x8x8 그리드 점을 생성합니다.

```python
x, y, z = np.indices((8, 8, 8))
```
