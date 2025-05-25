# 표면 정의

다음으로, 표면을 정의합니다. 이 예제에서는 `u`, `v` 쌍을 받아 `x`, `y`, `z` 삼중항을 반환하는 뫼비우스 매핑 (Mobius mapping) 을 사용합니다.

```python
x = (1 + 0.5 * v * np.cos(u / 2.0)) * np.cos(u)
y = (1 + 0.5 * v * np.cos(u / 2.0)) * np.sin(u)
z = 0.5 * v * np.sin(u / 2.0)
```
