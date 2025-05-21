# 끊어진 축 플롯에 마무리 작업 추가

이 마지막 단계에서는 y 축이 끊어졌음을 명확하게 하기 위해 끊어진 축 플롯에 마무리 작업을 추가합니다. 서브플롯 사이에 대각선을 추가하여 끊어진 부분을 표시하고, 적절한 레이블과 그리드를 사용하여 플롯의 전반적인 모양을 개선합니다.

## 대각선 끊기 선 추가

축이 끊어졌음을 시각적으로 나타내기 위해 두 서브플롯 사이에 대각선을 추가합니다. 이는 축의 일부가 생략되었음을 시청자가 이해하는 데 도움이 되는 일반적인 관례입니다.

새 셀을 만들고 다음 코드를 추가합니다.

```python
# Create two subplots stacked vertically with shared x-axis
fig, (ax1, ax2) = plt.subplots(2, 1, sharex=True, figsize=(8, 6))

# Plot the same data on both axes
ax1.plot(pts, 'o-', color='blue')
ax2.plot(pts, 'o-', color='blue')

# Set y-axis limits for each subplot
ax1.set_ylim(0.78, 1.0)    # Top subplot shows only the outliers
ax2.set_ylim(0, 0.22)      # Bottom subplot shows only the main data

# Hide the spines between ax1 and ax2
ax1.spines.bottom.set_visible(False)
ax2.spines.top.set_visible(False)

# Adjust the position of the ticks
ax1.xaxis.tick_top()          # Move x-axis ticks to the top
ax1.tick_params(labeltop=False)  # Hide x-axis tick labels at the top
ax2.xaxis.tick_bottom()       # Keep x-axis ticks at the bottom

# Add diagonal break lines
d = 0.5  # proportion of vertical to horizontal extent of the slanted line
kwargs = dict(marker=[(-1, -d), (1, d)], markersize=12,
              linestyle='none', color='k', mec='k', mew=1, clip_on=False)
ax1.plot([0, 1], [0, 0], transform=ax1.transAxes, **kwargs)
ax2.plot([0, 1], [1, 1], transform=ax2.transAxes, **kwargs)

# Add labels and a title
ax2.set_xlabel('Data Point Index')
ax2.set_ylabel('Value')
ax1.set_ylabel('Value')
fig.suptitle('Dataset with Outliers', fontsize=16)

# Add a grid to both subplots for better readability
ax1.grid(True, linestyle='--', alpha=0.7)
ax2.grid(True, linestyle='--', alpha=0.7)

plt.tight_layout()
plt.subplots_adjust(hspace=0.1)  # Adjust the space between subplots
plt.show()
```

이 셀을 실행하면 y 축의 끊어진 부분을 나타내는 대각선이 있는 완전한 끊어진 축 플롯을 볼 수 있습니다. 이제 플롯에는 가독성을 향상시키기 위한 제목, 축 레이블 및 그리드 선이 있습니다.

## 끊어진 축 플롯 이해

끊어진 축 플롯의 주요 구성 요소를 잠시 살펴보겠습니다.

1. **두 개의 서브플롯**: y 값의 서로 다른 범위에 각각 집중하는 두 개의 개별 서브플롯을 만들었습니다.
2. **숨겨진 스파인**: 시각적 분리를 만들기 위해 서브플롯 사이의 연결 스파인을 숨겼습니다.
3. **대각선 끊기 선**: 축이 끊어졌음을 나타내기 위해 대각선을 추가했습니다.
4. **Y 축 제한**: 데이터의 특정 부분에 집중하기 위해 각 서브플롯에 대해 서로 다른 y 축 제한을 설정했습니다.
5. **그리드 선**: 가독성을 높이고 값을 더 쉽게 추정할 수 있도록 그리드 선을 추가했습니다.

이 기술은 그렇지 않으면 대부분의 데이터 포인트의 시각화를 압축할 이상치가 데이터에 있는 경우에 특히 유용합니다. 축을 "끊음"으로써 단일 그림에서 이상치와 주 데이터 분포를 모두 명확하게 표시할 수 있습니다.

## 플롯 실험

이제 끊어진 축 플롯을 만드는 방법을 이해했으므로 다양한 구성으로 실험할 수 있습니다. y 축 제한을 변경하거나, 플롯에 더 많은 기능을 추가하거나, 이 기술을 자체 데이터에 적용해 보십시오.

예를 들어, 이전 코드를 수정하여 범례를 포함하거나, 색상 구성을 변경하거나, 마커 스타일을 조정할 수 있습니다.

```python
# Create two subplots stacked vertically with shared x-axis
fig, (ax1, ax2) = plt.subplots(2, 1, sharex=True, figsize=(8, 6))

# Plot the same data on both axes with different styles
ax1.plot(pts, 'o-', color='darkblue', label='Data Points', linewidth=2)
ax2.plot(pts, 'o-', color='darkblue', linewidth=2)

# Mark the outliers with a different color
outlier_indices = [3, 14]
ax1.plot(outlier_indices, pts[outlier_indices], 'ro', markersize=8, label='Outliers')

# Set y-axis limits for each subplot
ax1.set_ylim(0.78, 1.0)    # Top subplot shows only the outliers
ax2.set_ylim(0, 0.22)      # Bottom subplot shows only the main data

# Hide the spines between ax1 and ax2
ax1.spines.bottom.set_visible(False)
ax2.spines.top.set_visible(False)

# Adjust the position of the ticks
ax1.xaxis.tick_top()          # Move x-axis ticks to the top
ax1.tick_params(labeltop=False)  # Hide x-axis tick labels at the top
ax2.xaxis.tick_bottom()       # Keep x-axis ticks at the bottom

# Add diagonal break lines
d = 0.5  # proportion of vertical to horizontal extent of the slanted line
kwargs = dict(marker=[(-1, -d), (1, d)], markersize=12,
              linestyle='none', color='k', mec='k', mew=1, clip_on=False)
ax1.plot([0, 1], [0, 0], transform=ax1.transAxes, **kwargs)
ax2.plot([0, 1], [1, 1], transform=ax2.transAxes, **kwargs)

# Add labels and a title
ax2.set_xlabel('Data Point Index')
ax2.set_ylabel('Value')
ax1.set_ylabel('Value')
fig.suptitle('Dataset with Outliers - Enhanced Visualization', fontsize=16)

# Add a grid to both subplots for better readability
ax1.grid(True, linestyle='--', alpha=0.7)
ax2.grid(True, linestyle='--', alpha=0.7)

# Add a legend to the top subplot
ax1.legend(loc='upper right')

plt.tight_layout()
plt.subplots_adjust(hspace=0.1)  # Adjust the space between subplots
plt.show()
```

이 향상된 코드를 실행하면 이상치가 특별히 표시되고 데이터 포인트를 설명하는 범례가 있는 개선된 시각화를 볼 수 있습니다.

축하합니다! Matplotlib 을 사용하여 Python 에서 끊어진 축 플롯을 성공적으로 만들었습니다. 이 기술은 이상치를 포함하는 데이터를 처리할 때 더 효과적인 시각화를 만드는 데 도움이 됩니다.
