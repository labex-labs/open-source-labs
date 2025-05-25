# 3D 표면 플롯 생성

이제 3D 표면 플롯을 생성할 수 있습니다. 먼저 figure 를 생성하고 `projection='3d'` 인수를 사용하여 서브플롯을 추가합니다. 그런 다음, 이전 단계에서 생성한 데이터를 사용하여 `plot_surface()` 함수를 사용하여 표면을 플롯합니다.

```python
# Plot the surface
fig = plt.figure()
ax = fig.add_subplot(projection='3d')
ax.plot_surface(x, y, z)
```
