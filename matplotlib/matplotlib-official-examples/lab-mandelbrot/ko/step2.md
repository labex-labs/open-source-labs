# 만델브로 집합 함수 정의

다음으로, 만델브로 집합을 생성하는 함수를 정의합니다. 이 함수는 다음과 같은 여러 매개변수를 받습니다.

- `xmin`, `xmax`, `ymin`, `ymax`: x 및 y 축의 최소 및 최대 값
- `xn` 및 `yn`: 각 축을 따라 생성할 점의 수
- `maxiter`: 각 점에 대해 수행할 최대 반복 횟수
- `horizon`: 점이 집합의 일부로 간주될 최대 값

```python
def mandelbrot_set(xmin, xmax, ymin, ymax, xn, yn, maxiter, horizon=2.0):
    X = np.linspace(xmin, xmax, xn).astype(np.float32)
    Y = np.linspace(ymin, ymax, yn).astype(np.float32)
    C = X + Y[:, None] * 1j
    N = np.zeros_like(C, dtype=int)
    Z = np.zeros_like(C)
    for n in range(maxiter):
        I = abs(Z) < horizon
        N[I] = n
        Z[I] = Z[I]**2 + C[I]
    N[N == maxiter-1] = 0
    return Z, N
```
