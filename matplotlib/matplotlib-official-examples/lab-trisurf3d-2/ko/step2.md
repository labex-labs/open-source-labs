# 메쉬 생성

매개변수화 변수 `u`와 `v`의 공간에서 메쉬를 생성합니다. 이는 `np.meshgrid()` 함수를 사용하여 `u`와 `v` 점의 그리드를 생성하여 수행됩니다.

```python
u = np.linspace(0, 2.0 * np.pi, endpoint=True, num=50)
v = np.linspace(-0.5, 0.5, endpoint=True, num=10)
u, v = np.meshgrid(u, v)
u, v = u.flatten(), v.flatten()
```
