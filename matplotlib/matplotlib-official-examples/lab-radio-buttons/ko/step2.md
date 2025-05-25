# 데이터 생성

다음으로, 플롯에 사용될 데이터를 생성합니다. `numpy` 라이브러리를 사용하여 서로 다른 주파수를 가진 세 개의 서로 다른 사인파를 생성합니다.

```python
t = np.arange(0.0, 2.0, 0.01)
s0 = np.sin(2*np.pi*t)
s1 = np.sin(4*np.pi*t)
s2 = np.sin(8*np.pi*t)
```
