# 데이터 생성

다음으로, 플롯할 데이터를 생성해야 합니다. 별도의 figure 에 플롯할 두 개의 사인파를 생성합니다.

```python
t = np.arange(0.0, 2.0, 0.01)
s1 = np.sin(2*np.pi*t)
s2 = np.sin(4*np.pi*t)
```
