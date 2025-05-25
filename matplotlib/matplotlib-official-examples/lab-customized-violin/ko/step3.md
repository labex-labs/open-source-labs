# 바이올린 플롯 모양 사용자 정의

이제 바이올린 플롯의 모양을 사용자 정의합니다. 먼저, `showmeans`, `showmedians`, 및 `showextrema` 인수를 `False`로 설정하여 Matplotlib 가 그리는 내용을 제한합니다. 그런 다음, `set_facecolor` 및 `set_alpha` 메서드를 사용하여 바이올린 몸체의 색상과 불투명도를 변경합니다. 마지막으로, NumPy 의 `percentile` 함수를 사용하여 사분위수, 중앙값, 및 수염 (whiskers) 을 계산하여 바이올린 플롯 위에 상자 그림 (box plot) 의 단순화된 표현을 추가합니다.

```python
# customize violin plot appearance
fig, ax2 = plt.subplots()
ax2.set_title('Customized Violin Plot')
ax2.set_ylabel('Observed Values')

# create violin plot
parts = ax2.violinplot(
        data, showmeans=False, showmedians=False,
        showextrema=False)

# customize violin bodies
for pc in parts['bodies']:
    pc.set_facecolor('#D43F3A')
    pc.set_edgecolor('black')
    pc.set_alpha(1)

# add box plot
quartile1, medians, quartile3 = np.percentile(data, [25, 50, 75], axis=1)
whiskers = np.array([
    adjacent_values(sorted_array, q1, q3)
    for sorted_array, q1, q3 in zip(data, quartile1, quartile3)])
whiskers_min, whiskers_max = whiskers[:, 0], whiskers[:, 1]

inds = np.arange(1, len(medians) + 1)
ax2.scatter(inds, medians, marker='o', color='white', s=30, zorder=3)
ax2.vlines(inds, quartile1, quartile3, color='k', linestyle='-', lw=5)
ax2.vlines(inds, whiskers_min, whiskers_max, color='k', linestyle='-', lw=1)
```
