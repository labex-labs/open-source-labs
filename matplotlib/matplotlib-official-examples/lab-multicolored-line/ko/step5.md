# Colorbar 생성

색상과 `dydx` 값 사이의 매핑을 표시하기 위해 colorbar 를 생성합니다. `matplotlib.pyplot`의 `colorbar` 함수를 사용하여 colorbar 를 생성합니다.

```python
line = plt.gca().add_collection(lc)
plt.colorbar(line)
```
