# 무작위 데이터 생성

`numpy.random.random()`을 사용하여 무작위 데이터의 3D 배열을 생성합니다. 코드를 실행할 때마다 동일한 데이터 집합이 생성되도록 시드 값 (seed value) 을 사용합니다.

```python
np.random.seed(19680801)
data = np.random.random((50, 50, 50))
```
