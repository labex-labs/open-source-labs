# 컬러바가 있는 가장 간단한 해치 플롯

이 단계에서는 컬러바가 있는 가장 간단한 해치 플롯을 생성합니다. `contourf` 함수를 사용하여 채워진 등고선 플롯을 생성하고, `hatches` 매개변수를 사용하여 해치를 지정합니다.

```python
fig1, ax1 = plt.subplots()
cs = ax1.contourf(x, y, z, hatches=['-', '/', '\\', '//'],
                  cmap='gray', extend='both', alpha=0.5)
fig1.colorbar(cs)
```
