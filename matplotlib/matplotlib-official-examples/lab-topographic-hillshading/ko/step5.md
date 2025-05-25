# 플롯 생성

다양한 블렌드 모드 (blend mode) 와 수직 과장 (vertical exaggeration) 을 사용하여 음영 처리된 플롯을 표시하기 위해 4x3 플롯 그리드를 생성합니다. 먼저 첫 번째 행에 음영 처리된 강도 이미지를 표시한 다음, 나머지 행에 다양한 블렌드 모드를 가진 음영 처리된 플롯을 배치합니다. for 루프를 사용하여 서로 다른 수직 과장 값과 블렌드 모드를 반복합니다.

```python
fig, axs = plt.subplots(nrows=4, ncols=3, figsize=(8, 9))
plt.setp(axs.flat, xticks=[], yticks=[])

for col, ve in zip(axs.T, [0.1, 1, 10]):
    col[0].imshow(ls.hillshade(z, vert_exag=ve, dx=dx, dy=dy), cmap='gray')
    for ax, mode in zip(col[1:], ['hsv', 'overlay', 'soft']):
        rgb = ls.shade(z, cmap=cmap, blend_mode=mode,
                       vert_exag=ve, dx=dx, dy=dy)
        ax.imshow(rgb)
```
