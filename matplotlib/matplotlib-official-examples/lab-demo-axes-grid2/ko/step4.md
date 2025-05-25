# 데모 1 - 각 축에 컬러바 (Colorbar)

다음 코드를 사용하여 각 축에 컬러바가 있는 3 개의 이미지 그리드를 생성합니다.

```python
grid = ImageGrid(
    fig, 211, nrows_ncols=(1, 3), axes_pad=0.05, label_mode="1", share_all=True,
    cbar_location="top", cbar_mode="each", cbar_size="7%", cbar_pad="1%")
grid[0].set(xticks=[-2, 0], yticks=[-2, 0, 2])

for i, (ax, z) in enumerate(zip(grid, ZS)):
    im = ax.imshow(z, origin="lower", extent=extent)
    cb = ax.cax.colorbar(im)
    # Changing the colorbar ticks
    if i in [1, 2]:
        cb.set_ticks([-1, 0, 1])

for ax, im_title in zip(grid, ["Image 1", "Image 2", "Image 3"]):
    add_inner_title(ax, im_title, loc='lower left')
```

- `ImageGrid`를 사용하여 3 개의 이미지 그리드를 생성합니다.
- 각 축에 컬러바를 추가하기 위해 `cbar_mode`를 "each"로 설정합니다.
- 모든 이미지에서 x 및 y 축을 공유하기 위해 `share_all` 매개변수를 True 로 설정합니다.
- 컬러바를 상단에 배치하기 위해 `cbar_location` 매개변수를 "top"으로 설정합니다.
- 첫 번째 이미지에 대한 `xticks` 및 `yticks`를 설정합니다.
- 각 이미지를 반복하고 `imshow`를 사용하여 이미지를 축에 추가합니다.
- `ax.cax.colorbar`를 사용하여 각 축에 컬러바를 추가합니다.
- 두 번째 및 세 번째 이미지에 대한 컬러바 눈금을 설정합니다.
- `add_inner_title`을 사용하여 각 이미지에 제목을 추가합니다.
