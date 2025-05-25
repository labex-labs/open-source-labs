# 플롯 생성

먼저 MandelbrotDisplay 클래스를 사용하여 이미지를 계산한 다음, subplots 를 사용하여 두 개의 동일한 패널을 생성하여 플롯을 생성합니다. imshow 를 사용하여 두 패널 모두에 이미지를 추가하고, UpdatingRect 객체를 왼쪽 패널에 추가합니다.

```python
md = MandelbrotDisplay()
Z = md.compute_image(-2., 0.5, -1.25, 1.25)

fig1, (ax1, ax2) = plt.subplots(1, 2)
ax1.imshow(Z, origin='lower',
           extent=(md.x.min(), md.x.max(), md.y.min(), md.y.max()))
ax2.imshow(Z, origin='lower',
           extent=(md.x.min(), md.x.max(), md.y.min(), md.y.max()))

rect = UpdatingRect(
    [0, 0], 0, 0, facecolor='none', edgecolor='black', linewidth=1.0)
rect.set_bounds(*ax2.viewLim.bounds)
ax1.add_patch(rect)
```
