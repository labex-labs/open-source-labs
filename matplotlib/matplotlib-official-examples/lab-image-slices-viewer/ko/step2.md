# 데이터 생성

NumPy 의 `ogrid` 함수를 사용하여 3D 데이터를 생성합니다.

```python
x, y, z = np.ogrid[-10:10:100j, -10:10:100j, 1:10:20j]
X = np.sin(x * y * z) / (x * y * z)
```
