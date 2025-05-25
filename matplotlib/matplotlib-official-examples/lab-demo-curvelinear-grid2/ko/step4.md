# 축 정의 및 이미지 표시

네 번째 단계는 3 단계에서 생성된 `grid_helper` 인스턴스를 사용하여 축을 정의하는 것입니다. 또한 `imshow` 함수를 사용하여 이미지를 표시합니다.

```python
ax1 = fig.add_subplot(axes_class=Axes, grid_helper=grid_helper)
ax1.imshow(np.arange(25).reshape(5, 5), vmax=50, cmap=plt.cm.gray_r, origin="lower")
```
