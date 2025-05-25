# 음영 기복 플롯 생성

이제 `LightSource` 클래스를 사용하여 음영 기복 플롯을 생성합니다. 컬러맵 데이터가 있는 서브플롯 하나와 조명 강도가 있는 다른 서브플롯, 총 두 개의 서브플롯을 생성합니다.

```python
# Illuminate the scene from the northwest
ls = LightSource(azdeg=315, altdeg=45)

fig, axs = plt.subplots(ncols=2, nrows=2)
for ax in axs.flat:
    ax.set(xticks=[], yticks=[])

axs[0, 0].imshow(z, cmap=cmap)
axs[0, 0].set(xlabel='Colormapped Data')

axs[0, 1].imshow(ls.hillshade(z, vert_exag=ve), cmap='gray')
axs[0, 1].set(xlabel='Illumination Intensity')
```

`blend_mode`를 "hsv"로 설정한 서브플롯 하나와 "overlay"로 설정한 다른 서브플롯, 총 두 개의 서브플롯을 더 생성합니다.

```python
rgb = ls.shade(z, cmap=cmap, vert_exag=ve, blend_mode='hsv')
axs[1, 0].imshow(rgb)
axs[1, 0].set(xlabel='Blend Mode: "hsv" (default)')

rgb = ls.shade(z, cmap=cmap, vert_exag=ve, blend_mode='overlay')
axs[1, 1].imshow(rgb)
axs[1, 1].set(xlabel='Blend Mode: "overlay"')
```
