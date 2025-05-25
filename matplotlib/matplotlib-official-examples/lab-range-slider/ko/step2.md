# 이미지 및 히스토그램 표시

다음으로, Matplotlib 의 `imshow` 함수를 사용하여 이미지를 표시하고, `hist`를 사용하여 히스토그램을 표시합니다. 이미지와 히스토그램을 위한 두 개의 서브플롯 (subplot) 이 있는 figure 를 생성합니다.

```python
fig, axs = plt.subplots(1, 2, figsize=(10, 5))
fig.subplots_adjust(bottom=0.25)

im = axs[0].imshow(img)
axs[1].hist(img.flatten(), bins='auto')
axs[1].set_title('Histogram of pixel intensities')
```
