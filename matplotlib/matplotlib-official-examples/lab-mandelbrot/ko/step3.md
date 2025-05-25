# 만델브로 집합 생성

이제 원하는 매개변수를 사용하여 `mandelbrot_set` 함수를 호출하여 만델브로 집합을 생성합니다. 이렇게 하면 두 개의 배열이 생성됩니다.

- `Z`: 반복한 복소수의 최종 값
- `N`: 집합의 일부로 결정되기 전에 각 점에 대해 수행된 반복 횟수

```python
xmin, xmax, xn = -2.25, +0.75, 3000 // 2
ymin, ymax, yn = -1.25, +1.25, 2500 // 2
maxiter = 200
horizon = 2.0 ** 40
log_horizon = np.log2(np.log(horizon))
Z, N = mandelbrot_set(xmin, xmax, ymin, ymax, xn, yn, maxiter, horizon)
```
