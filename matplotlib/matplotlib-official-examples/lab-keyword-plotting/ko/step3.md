# 데이터 생성

이 단계에서는 변수 `a`, `b`, `c`, `d`의 값을 포함하는 딕셔너리 `data`를 생성합니다.

```python
data = {'a': np.arange(50),
        'c': np.random.randint(0, 50, 50),
        'd': np.random.randn(50)}

data['b'] = data['a'] + 10 * np.random.randn(50)
data['d'] = np.abs(data['d']) * 100
```
