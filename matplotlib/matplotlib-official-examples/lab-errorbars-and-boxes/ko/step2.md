# 데이터 준비

그런 다음 상자 그림에 사용할 데이터를 준비합니다. x 및 y 값과 오차 값에 대한 더미 데이터를 생성합니다.

```python
# 데이터 포인트 수
n = 5

# 더미 데이터
np.random.seed(19680801)
x = np.arange(0, n, 1)
y = np.random.rand(n) * 5.

# 더미 오차 (위와 아래)
xerr = np.random.rand(2, n) + 0.1
yerr = np.random.rand(2, n) + 0.2
```
