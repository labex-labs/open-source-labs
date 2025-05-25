# 정사각형 결합/주변 분포 플롯

결합 데이터 플롯 옆에 주변 분포를 표시하는 것이 바람직할 수 있습니다. 다음은 주변 축의 박스 종횡비가 gridspec 의 너비 및 높이 비율과 동일한 정사각형 플롯을 생성합니다. 이렇게 하면 그림 크기에 관계없이 모든 축이 완벽하게 정렬됩니다.

```python
fig5, axs = plt.subplots(2, 2, sharex="col", sharey="row",
                         gridspec_kw=dict(height_ratios=[1, 3],
                                          width_ratios=[3, 1]))
axs[0, 1].set_visible(False)
axs[0, 0].set_box_aspect(1/3)
axs[1, 0].set_box_aspect(1)
axs[1, 1].set_box_aspect(3/1)

np.random.seed(19680801)  # Fixing random state for reproducibility
x, y = np.random.randn(2, 400) * [[.5], [180]]
axs[1, 0].scatter(x, y)
axs[0, 0].hist(x)
axs[1, 1].hist(y, orientation="horizontal")

plt.show()
```
