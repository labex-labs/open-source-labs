# 플롯 애니메이션

다섯 번째 단계는 플롯을 애니메이션하는 것입니다. for 루프를 사용하여 phi 값의 범위를 반복합니다. 각 반복에서 이전 선 컬렉션을 제거하고, 새로운 데이터를 생성하고, 새로운 와이어프레임을 플롯하고, 잠시 멈춘 후 계속 진행합니다.

```python
wframe = None
tstart = time.time()
for phi in np.linspace(0, 180. / np.pi, 100):
    if wframe:
        wframe.remove()
    Z = np.cos(2 * np.pi * X + phi) * (1 - np.hypot(X, Y))
    wframe = ax.plot_wireframe(X, Y, Z, rstride=2, cstride=2)
    plt.pause(.001)
```
