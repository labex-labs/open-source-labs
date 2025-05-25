# 함수 정의

애플리케이션이 표시할 함수 목록을 정의합니다. 각 함수는 math text 와 입력 값을 받아 출력 값을 반환하는 lambda 함수로 정의됩니다.

```python
functions = [
    (r'$\sin(2 \pi x)$', lambda x: np.sin(2*np.pi*x)),
    (r'$\frac{4}{3}\pi x^3$', lambda x: (4/3)*np.pi*x**3),
    (r'$\cos(2 \pi x)$', lambda x: np.cos(2*np.pi*x)),
    (r'$\log(x)$', lambda x: np.log(x))
]
```
