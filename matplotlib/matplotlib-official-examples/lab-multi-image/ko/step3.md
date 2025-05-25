# 색상 척도 설정 및 Colorbar 생성

이제 이미지의 색상 척도를 설정하고 값의 범위를 표시하기 위해 colorbar 를 생성합니다. 모든 이미지에 대한 최소 및 최대 값을 찾아 그에 따라 색상 척도를 정규화합니다.

```python
vmin = min(image.get_array().min() for image in images)
vmax = max(image.get_array().max() for image in images)
norm = colors.Normalize(vmin=vmin, vmax=vmax)
for im in images:
    im.set_norm(norm)

fig.colorbar(images[0], ax=axs, orientation='horizontal', fraction=.1)
```
