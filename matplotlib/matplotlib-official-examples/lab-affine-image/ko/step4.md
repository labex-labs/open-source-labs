# 이미지 기울이기 수행

이 단계에서는 `skew_deg` 함수를 사용하여 이미지 기울이기를 수행합니다. 기울이기 각도를 `skew_deg` 함수에 입력으로 전달합니다. 기울여진 이미지를 표시하기 위해 `do_plot` 함수를 사용합니다.

```python
# prepare image and figure
fig, ax2 = plt.subplots()
Z = get_image()

# image skew
do_plot(ax2, Z, mtransforms.Affine2D().skew_deg(30, 15))
```
