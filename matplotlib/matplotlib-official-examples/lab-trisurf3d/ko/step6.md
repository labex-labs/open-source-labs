# 3D 표면 생성

`plot_trisurf` 함수를 사용하여 3D 표면을 생성합니다:

```python
ax = plt.figure().add_subplot(projection='3d')
ax.plot_trisurf(x, y, z, linewidth=0.2, antialiased=True)

plt.show()
```
