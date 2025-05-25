# 플롯 생성

이제 `plt.subplots()` 함수를 사용하여 플롯을 생성할 수 있습니다. 이 예제에서는 간단한 선 그래프를 생성합니다.

```python
fig, ax = plt.subplots(figsize=(4.5, 2.5))

ax.plot(range(5))
```
