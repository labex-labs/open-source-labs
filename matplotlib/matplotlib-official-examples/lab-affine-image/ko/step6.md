# 다중 변환 수행

이 단계에서는 `rotate_deg`, `skew_deg`, `scale`, 및 `translate` 함수를 사용하여 이미지에 대한 다중 변환을 수행합니다. 변환 매개변수를 각 함수에 입력으로 전달합니다. 변환된 이미지를 표시하기 위해 `do_plot` 함수를 사용합니다.

```python
# prepare image and figure
fig, ax4 = plt.subplots()
Z = get_image()

# everything and a translation
do_plot(ax4, Z, mtransforms.Affine2D().
        rotate_deg(30).skew_deg(30, 15).scale(-1, .5).translate(.5, -1))
```
