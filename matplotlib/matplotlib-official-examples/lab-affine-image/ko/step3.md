# 이미지 회전 수행

이 단계에서는 `rotate_deg` 함수를 사용하여 이미지 회전을 수행합니다. 회전 각도를 `rotate_deg` 함수에 입력으로 전달합니다. 회전된 이미지를 표시하기 위해 `do_plot` 함수를 사용합니다.

```python
# prepare image and figure
fig, ax1 = plt.subplots()
Z = get_image()

# image rotation
do_plot(ax1, Z, mtransforms.Affine2D().rotate_deg(30))
```
