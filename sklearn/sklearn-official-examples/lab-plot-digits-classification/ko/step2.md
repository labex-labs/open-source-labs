# 숫자 데이터셋 로드 및 시각화

8x8 픽셀 이미지로 구성된 숫자 데이터셋을 로드합니다. `matplotlib`의 `imshow()` 메서드를 사용하여 첫 4 개 이미지와 해당 레이블을 시각화합니다.

```python
digits = datasets.load_digits()

_, axes = plt.subplots(nrows=1, ncols=4, figsize=(10, 3))
for ax, image, label in zip(axes, digits.images, digits.target):
    ax.set_axis_off()
    ax.imshow(image, cmap=plt.cm.gray_r, interpolation="nearest")
    ax.set_title("Training: %i" % label)
```
