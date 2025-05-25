# 표면 플롯

```python
surf = ax.plot_surface(X, Y, Z, cmap=cm.coolwarm,
                       linewidth=0, antialiased=False)
```

`plot_surface()` 함수를 사용하여 표면을 플롯합니다. `X`, `Y`, `Z` 값과 함께 `cmap` 매개변수를 `cm.coolwarm`으로 설정하여 coolwarm colormap 으로 표면의 색상을 지정합니다. 또한 wireframe 을 제거하기 위해 `linewidth=0`으로 설정하고, 표면을 불투명하게 만들기 위해 `antialiased=False`로 설정합니다.
