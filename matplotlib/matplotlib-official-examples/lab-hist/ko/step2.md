# 히스토그램 색상 업데이트

히스토그램 메서드는 (다른 것들 중에서) `patches` 객체를 반환합니다. 이를 통해 그려진 객체의 속성에 액세스할 수 있습니다. 이를 사용하여 원하는 대로 히스토그램을 편집할 수 있습니다. 각 막대의 색상을 y 값에 따라 변경해 보겠습니다.

```python
# N 은 각 bin 의 개수이고, bins 는 bin 의 하한입니다.
N, bins, patches = axs[0].hist(dist1, bins=n_bins)

# 높이에 따라 색상을 지정하지만, 임의의 스칼라를 사용할 수 있습니다.
fracs = N / N.max()

# colormap 의 전체 범위를 위해 데이터를 0..1 로 정규화해야 합니다.
norm = colors.Normalize(fracs.min(), fracs.max())

# 이제 객체를 반복하고 각 객체의 색상을 적절하게 설정합니다.
for thisfrac, thispatch in zip(fracs, patches):
    color = plt.cm.viridis(norm(thisfrac))
    thispatch.set_facecolor(color)

# 총 개수로 입력을 정규화할 수도 있습니다.
axs[1].hist(dist1, bins=n_bins, density=True)

# 이제 y 축을 형식화하여 백분율을 표시합니다.
axs[1].yaxis.set_major_formatter(PercentFormatter(xmax=1))

plt.show()
```
