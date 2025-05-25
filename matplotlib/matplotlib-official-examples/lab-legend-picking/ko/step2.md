# 데이터 준비

NumPy 를 사용하여 서로 다른 주파수를 가진 두 개의 사인파를 생성합니다.

```python
t = np.linspace(0, 1)
y1 = 2 * np.sin(2*np.pi*t)
y2 = 4 * np.sin(2*np.pi*2*t)
```
