# 데이터 생성

다음으로, 플롯에 사용할 데이터를 생성합니다. 이 예제에서는 서로 다른 주파수를 가진 세 개의 사인파를 생성합니다.

```python
t = np.arange(0.0, 2.0, 0.01)
s1 = np.sin(2*np.pi*t)
s2 = np.sin(3*np.pi*t)
s3 = np.sin(4*np.pi*t)
```
