# 이미지 옆의 일반 플롯

고정된 데이터 종횡비 (data aspect) 와 기본 `adjustable="box"`를 사용하여 일반 플롯 옆에 이미지 플롯을 생성할 때, 축의 높이가 서로 다르게 됩니다. `set_box_aspect()`는 일반 플롯의 축이 이미지의 차원을 박스 종횡비로 사용하도록 허용하여 이에 대한 쉬운 해결책을 제공합니다. 이 예제는 또한 *constrained layout*이 고정된 박스 종횡비와 잘 상호 작용한다는 것을 보여줍니다.

```python
fig4, (ax, ax2) = plt.subplots(ncols=2, layout="constrained")

np.random.seed(19680801)  # Fixing random state for reproducibility
im = np.random.rand(16, 27)
ax.imshow(im)

ax2.plot([23, 45])
ax2.set_box_aspect(im.shape[0]/im.shape[1])

plt.show()
```
