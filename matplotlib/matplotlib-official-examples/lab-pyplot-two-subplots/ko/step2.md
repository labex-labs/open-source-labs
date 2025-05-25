# 데이터 정의

서브플롯을 생성하는 데 사용할 두 개의 데이터 세트를 정의합니다.

```python
def f(t):
    return np.exp(-t) * np.cos(2*np.pi*t)

t1 = np.arange(0.0, 5.0, 0.1)
t2 = np.arange(0.0, 5.0, 0.02)
```
