# 플롯 생성

이제 데이터를 얻었으므로 와이어프레임 플롯을 생성할 수 있습니다. 이 예제에서는 `plot_wireframe()` 함수를 사용하여 플롯을 생성합니다.

```python
# Create the plot
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
ax.plot_wireframe(X, Y, Z, rstride=5, cstride=5)
```
