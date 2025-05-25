# Gouraud Shading (고라우드 쉐이딩)

`Gouraud shading`도 지정할 수 있으며, 여기서 사변형의 색상은 그리드 포인트 사이에서 선형적으로 보간됩니다. `X`, `Y`, `Z`의 형태는 동일해야 합니다. 다음 코드 블록을 사용하여 그리드를 시각화할 수 있습니다.

```python
fig, ax = plt.subplots()
ax.pcolormesh(X, Y, Z, shading='gouraud', cmap='viridis')
ax.set_title('Gouraud Shading')
plt.show()
```
