# 더 나은 금융 데이터 시각화를 위한 플롯 개선

이제 기본적인 통화 서식이 적용되었으므로, 금융 데이터 분석에 더 유용하도록 플롯을 추가로 개선해 보겠습니다. 다음과 같은 몇 가지 개선 사항을 추가합니다.

1. 평균 일일 수익을 보여주는 수평선
2. 최대 및 최소 수익일을 강조 표시하는 주석
3. 가독성을 높이기 위한 사용자 지정 눈금 매개변수
4. 더 설명적인 제목과 범례

노트북의 새 셀에 다음 코드를 추가하고 실행합니다.

```python
# Import the necessary module for formatting
import matplotlib.ticker as ticker

# Create a figure and axes
fig, ax = plt.subplots(figsize=(12, 7))

# Plot the daily revenue data
ax.plot(days, daily_revenue, marker='o', linestyle='-', color='blue',
        linewidth=2, markersize=6, label='Daily Revenue')

# Calculate statistics
avg_revenue = np.mean(daily_revenue)
max_revenue = np.max(daily_revenue)
min_revenue = np.min(daily_revenue)
max_day = days[np.argmax(daily_revenue)]
min_day = days[np.argmin(daily_revenue)]

# Add a horizontal line for average revenue
ax.axhline(y=avg_revenue, color='r', linestyle='--', alpha=0.7,
           label=f'Average Revenue: ${avg_revenue:.2f}')

# Format y-axis with dollar signs
formatter = ticker.StrMethodFormatter('${x:,.2f}')
ax.yaxis.set_major_formatter(formatter)

# Customize tick parameters
ax.tick_params(axis='both', which='major', labelsize=10)
ax.yaxis.set_major_locator(ticker.MaxNLocator(nbins=10))
ax.xaxis.set_major_locator(ticker.MultipleLocator(base=5))

# Add annotations for max and min revenue
ax.annotate(f'Max: ${max_revenue:.2f}', xy=(max_day, max_revenue),
            xytext=(max_day+1, max_revenue+200),
            arrowprops=dict(facecolor='black', shrink=0.05, width=1.5))

ax.annotate(f'Min: ${min_revenue:.2f}', xy=(min_day, min_revenue),
            xytext=(min_day+1, min_revenue-200),
            arrowprops=dict(facecolor='black', shrink=0.05, width=1.5))

# Add labels and title
ax.set_xlabel('Day of Month', fontsize=12)
ax.set_ylabel('Revenue ($)', fontsize=12)
ax.set_title('Daily Revenue Analysis - 30 Day Period', fontsize=14, fontweight='bold')

# Set x-axis limits to show a bit of padding
ax.set_xlim(0, 31)

# Add grid for better readability
ax.grid(True, linestyle='--', alpha=0.7)

# Add legend
ax.legend(loc='upper right', fontsize=10)

# Display the plot
plt.tight_layout()
plt.show()

print("Enhanced financial plot created successfully!")
```

이 코드를 실행하면 다음과 같은 훨씬 더 유익한 플롯이 표시됩니다.

1. y 축에 달러 기호 서식
2. 평균 수익을 보여주는 수평 빨간색 점선
3. 최대 및 최소 수익일을 가리키는 주석
4. 더 나은 간격의 더 깨끗한 눈금 표시
5. 각 요소가 무엇을 나타내는지 보여주는 범례

새로운 요소 중 일부를 설명해 보겠습니다.

- `ax.axhline()` - 지정된 y 값 (이 경우 평균 수익) 에 수평선을 추가합니다.
- `ax.yaxis.set_major_locator()` - y 축에 표시되는 눈금 표시의 수를 제어합니다.
- `ax.xaxis.set_major_locator()` - x 축이 5 일 간격으로 눈금을 표시하도록 설정합니다.
- `ax.annotate()` - 특정 데이터 포인트를 가리키는 화살표가 있는 텍스트 주석을 추가합니다.
- `ax.legend()` - 플롯의 다른 요소를 설명하는 범례를 추가합니다.

이러한 개선 사항은 주요 통계를 강조 표시하고 데이터를 더 쉽게 해석할 수 있도록 하여 금융 분석에 플롯을 훨씬 더 유용하게 만듭니다.
