# 임의 데이터 생성

이 단계에서는 산점도에 사용할 임의 데이터를 생성합니다. NumPy 라이브러리를 사용하여 각 변수에 대해 50 개의 데이터 포인트를 생성합니다.

```python
np.random.seed(19680801)

N = 50
x = np.random.rand(N)
y = np.random.rand(N)
```
