# 히스토그램 사용자 정의

2D 히스토그램을 사용자 정의하는 것은 1D 경우와 유사하며, bin 크기 또는 색상 정규화와 같은 시각적 구성 요소를 제어할 수 있습니다.

```python
fig, axs = plt.subplots(3, 1, figsize=(5, 15), sharex=True, sharey=True,
                        tight_layout=True)

# 각 축에서 bin 의 수를 늘릴 수 있습니다.
axs[0].hist2d(dist1, dist2, bins=40)

# 색상의 정규화도 정의할 수 있습니다.
axs[1].hist2d(dist1, dist2, bins=40, norm=colors.LogNorm())

# 각 축에 대해 사용자 정의 bin 수를 정의할 수도 있습니다.
axs[2].hist2d(dist1, dist2, bins=(80, 10), norm=colors.LogNorm())

plt.show()
```
