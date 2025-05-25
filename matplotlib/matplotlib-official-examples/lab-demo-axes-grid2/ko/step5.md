# 데모 2 - 공유 컬러바 (Shared Colorbar)

다음 코드를 사용하여 공유 컬러바가 있는 3 개의 이미지 그리드를 생성합니다.

```python
grid2 = ImageGrid(
    fig, 212, nrows_ncols=(1, 3), axes_pad=0.05, label_mode="1", share_all=True,
    cbar_location="right", cbar_mode="single", cbar_size="10%", cbar_pad=0.05)
grid2[0].set(xlabel="X", ylabel="Y", xticks=[-2, 0], yticks=[-2, 0, 2])

clim = (np.min(ZS), np.max(ZS))
for ax, z in zip(grid2, ZS):
    im = ax.imshow(z, clim=clim, origin="lower", extent=extent)

# With cbar_mode="single", cax attribute of all axes are identical.
ax.cax.colorbar(im)

for ax, im_title in zip(grid2, ["(a)", "(b)", "(c)"]):
    add_inner_title(ax, im_title, loc='upper left')
```

- `ImageGrid`를 사용하여 3 개의 이미지 그리드를 생성합니다.
- 공유 컬러바를 추가하기 위해 `cbar_mode`를 "single"로 설정합니다.
- 모든 이미지에서 x 및 y 축을 공유하기 위해 `share_all` 매개변수를 True 로 설정합니다.
- 컬러바를 오른쪽에 배치하기 위해 `cbar_location` 매개변수를 "right"로 설정합니다.
- 첫 번째 이미지에 대한 `xticks` 및 `yticks`를 설정합니다.
- 각 이미지를 반복하고 `imshow`를 사용하여 이미지를 축에 추가합니다.
- 모든 이미지가 동일한 색상 스케일을 사용하도록 `clim` 매개변수를 설정합니다.
- `ax.cax.colorbar`를 사용하여 축에 공유 컬러바를 추가합니다.
- `add_inner_title`을 사용하여 각 이미지에 제목을 추가합니다.
