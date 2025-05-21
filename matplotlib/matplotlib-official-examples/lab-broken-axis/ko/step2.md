# 끊어진 축 플롯 생성 및 구성

이 단계에서는 실제 끊어진 축 플롯 구조를 생성합니다. 끊어진 축 플롯은 동일한 데이터의 서로 다른 범위를 보여주는 여러 개의 서브플롯으로 구성됩니다. 주 데이터와 이상치를 효과적으로 표시하도록 이러한 서브플롯을 구성합니다.

## 서브플롯 생성

먼저, 수직으로 정렬된 두 개의 서브플롯을 생성해야 합니다. 상단 서브플롯은 이상치를 표시하고, 하단 서브플롯은 대부분의 데이터 포인트를 표시합니다.

노트북에서 새 셀을 만들고 다음 코드를 추가합니다.

```python
# Create two subplots stacked vertically with shared x-axis
fig, (ax1, ax2) = plt.subplots(2, 1, sharex=True, figsize=(8, 6))

# Add a main title to the figure
fig.suptitle('Broken Axis Plot Example', fontsize=16)

# Plot the same data on both axes
ax1.plot(pts, 'o-', color='blue')
ax2.plot(pts, 'o-', color='blue')

# Display the figure to see both subplots
plt.tight_layout()
plt.show()
```

![broken-axis-plot](../assets/screenshot-20250306-cawcMZv3@2x.png)

이 셀을 실행하면 두 개의 서브플롯이 있는 그림이 표시되며, 두 서브플롯 모두 동일한 데이터를 표시합니다. 이상치가 두 플롯 모두에서 나머지 데이터를 압축하여 대부분의 데이터 포인트의 세부 정보를 보기 어렵게 만드는 것을 확인하십시오. 이것이 바로 끊어진 축 플롯으로 해결하려는 문제입니다.

## Y 축 제한 구성

이제 각 서브플롯이 특정 y 값 범위에 집중하도록 구성해야 합니다. 상단 서브플롯은 이상치 범위에 집중하고, 하단 서브플롯은 주 데이터 범위에 집중합니다.

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

# Add a title to each subplot
ax1.set_title('Outlier Region')
ax2.set_title('Main Data Region')

# Display the figure with adjusted y-axis limits
plt.tight_layout()
plt.show()
```

이 셀을 실행하면 각 서브플롯이 이제 서로 다른 y 값 범위에 집중하는 것을 볼 수 있습니다. 상단 플롯은 이상치만 표시하고, 하단 플롯은 주 데이터만 표시합니다. 이것은 이미 시각화를 개선하지만, 제대로 된 끊어진 축 플롯을 만들려면 몇 가지 더 많은 구성을 추가해야 합니다.

## 스파인 숨기기 및 눈금 조정

"끊어진" 축의 환상을 만들기 위해 두 서브플롯 사이의 연결 스파인을 숨기고 눈금 위치를 조정해야 합니다.

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

# Add labels to the plot
ax2.set_xlabel('Data Point Index')
ax2.set_ylabel('Value')
ax1.set_ylabel('Value')

plt.tight_layout()
plt.show()
```

이 셀을 실행하면 이제 두 서브플롯 사이에 숨겨진 스파인이 있어 더 깔끔한 모양을 만드는 플롯을 볼 수 있습니다. x 축 눈금은 이제 올바르게 배치되어 있으며, 레이블은 하단에만 있습니다.

이 시점에서 기본 끊어진 축 플롯을 성공적으로 만들었습니다. 다음 단계에서는 시청자가 축이 끊어졌음을 명확하게 알 수 있도록 마무리 작업을 추가합니다.
