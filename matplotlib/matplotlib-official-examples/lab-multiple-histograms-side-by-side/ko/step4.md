# 히스토그램 플롯

플로팅에 필요한 값을 계산했으므로, 이제 히스토그램을 생성할 수 있습니다. 각 히스토그램에 대해 수평 막대를 플롯하기 위해 `barh` 메서드를 사용합니다.

```python
# The bin_edges are the same for all of the histograms
bin_edges = np.linspace(hist_range[0], hist_range[1], number_of_bins + 1)
heights = np.diff(bin_edges)
centers = bin_edges[:-1] + heights / 2

# Cycle through and plot each histogram
fig, ax = plt.subplots()
for x_loc, binned_data in zip(x_locations, binned_data_sets):
    lefts = x_loc - 0.5 * binned_data
    ax.barh(centers, binned_data, height=heights, left=lefts)

ax.set_xticks(x_locations, labels)
ax.set_ylabel("Data values")
ax.set_xlabel("Data sets")
```
