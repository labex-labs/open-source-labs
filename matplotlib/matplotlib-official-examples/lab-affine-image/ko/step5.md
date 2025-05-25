# 이미지 크기 조정 및 반사 수행

이 단계에서는 `scale` 함수를 사용하여 이미지의 크기 조정 및 반사를 수행합니다. 크기 조정 및 반사 인자를 `scale` 함수에 입력으로 전달합니다. 크기 조정 및 반사된 이미지를 표시하기 위해 `do_plot` 함수를 사용합니다.

```python
# prepare image and figure
fig, ax3 = plt.subplots()
Z = get_image()

# scale and reflection
do_plot(ax3, Z, mtransforms.Affine2D().scale(-1, .5))
```
