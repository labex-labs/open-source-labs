# 3D 줄기 플롯 생성

이 단계에서는 Matplotlib 의 `stem` 함수를 사용하여 3D 줄기 플롯을 생성합니다. `stem` 함수에 x, y, z 좌표를 인수로 전달합니다.

```python
fig, ax = plt.subplots(subplot_kw=dict(projection='3d'))
ax.stem(x, y, z)

plt.show()
```
