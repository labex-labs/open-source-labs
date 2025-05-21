# 여러 텍스트 요소를 사용하여 최종 시각화 생성

이 마지막 단계에서는 배운 모든 것을 결합하여 다양한 스타일의 여러 텍스트 요소를 포함하는 포괄적인 시각화를 생성합니다. 이는 텍스트 상자를 사용하여 데이터 스토리텔링을 향상시키는 방법을 보여줍니다.

## 고급 시각화 생성

히스토그램과 몇 가지 추가 시각적 요소를 모두 포함하는 더 정교한 플롯을 만들어 보겠습니다. 새 셀에 다음 코드를 입력하고 실행합니다.

```python
# Create a figure with a larger size for our final visualization
fig, ax = plt.subplots(figsize=(12, 8))

# Plot the histogram with more bins and a different color
n, bins, patches = ax.hist(x, bins=75, color='lightblue',
                           edgecolor='darkblue', alpha=0.7)

# Add title and labels with improved styling
ax.set_title('Distribution of Random Data with Statistical Annotations',
             fontsize=18, fontweight='bold', pad=20)
ax.set_xlabel('Value', fontsize=14)
ax.set_ylabel('Frequency', fontsize=14)

# Add grid for better readability
ax.grid(True, linestyle='--', alpha=0.7)

# Mark the mean with a vertical line
ax.axvline(x=mu, color='red', linestyle='-', linewidth=2,
           label=f'Mean: {mu:.2f}')

# Mark one standard deviation range
ax.axvline(x=mu + sigma, color='green', linestyle='--', linewidth=1.5,
           label=f'Mean + 1σ: {mu+sigma:.2f}')
ax.axvline(x=mu - sigma, color='green', linestyle='--', linewidth=1.5,
           label=f'Mean - 1σ: {mu-sigma:.2f}')

# Create a text box with statistics in the top left
stats_box_props = dict(boxstyle='round', facecolor='lightyellow',
                      alpha=0.8, edgecolor='gold', linewidth=2)

stats_text = '\n'.join((
    r'$\mathbf{Statistics:}$',
    r'$\mu=%.2f$ (mean)' % (mu,),
    r'$\mathrm{median}=%.2f$' % (median,),
    r'$\sigma=%.2f$ (std. dev.)' % (sigma,)
))

ax.text(0.05, 0.95, stats_text, transform=ax.transAxes, fontsize=14,
        verticalalignment='top', bbox=stats_box_props)

# Add an informational text box in the top right
info_box_props = dict(boxstyle='round4', facecolor='lightcyan',
                     alpha=0.8, edgecolor='deepskyblue', linewidth=2)

info_text = '\n'.join((
    r'$\mathbf{About\ Normal\ Distributions:}$',
    r'$\bullet\ 68\%\ of\ data\ within\ 1\sigma$',
    r'$\bullet\ 95\%\ of\ data\ within\ 2\sigma$',
    r'$\bullet\ 99.7\%\ of\ data\ within\ 3\sigma$'
))

ax.text(0.95, 0.95, info_text, transform=ax.transAxes, fontsize=14,
        verticalalignment='top', horizontalalignment='right',
        bbox=info_box_props)

# Add a legend
ax.legend(fontsize=12)

# Tighten the layout and show the plot
plt.tight_layout()
plt.show()
```

이 셀을 실행하면 다음이 포함된 포괄적인 시각화가 표시됩니다.

- 스타일이 개선된 데이터의 히스토그램
- 평균 및 표준 편차 범위를 표시하는 수직선
- 왼쪽 상단 모서리에 있는 통계 텍스트 상자
- 오른쪽 상단 모서리에 있는 정규 분포에 대한 정보 텍스트 상자
- 수직선을 설명하는 범례

## 고급 요소 이해

추가한 몇 가지 새로운 요소를 살펴보겠습니다.

1. **`axvline()`을 사용한 수직선**:

   - 이러한 선은 플롯에 직접 중요한 통계를 표시합니다.
   - `label` 매개변수를 사용하면 이러한 선을 범례에 포함할 수 있습니다.

2. **다양한 스타일의 여러 텍스트 상자**:

   - 각 텍스트 상자는 다른 목적을 수행하고 고유한 스타일을 사용합니다.
   - 통계 상자는 데이터에서 계산된 값을 표시합니다.
   - 정보 상자는 정규 분포에 대한 컨텍스트를 제공합니다.

3. **향상된 서식**:

   - LaTeX 서식은 `\mathbf{}`를 사용하여 굵은 텍스트를 생성하는 데 사용됩니다.
   - 글머리 기호는 `\bullet`로 생성됩니다.
   - 간격은 `\ `(백슬래시 뒤에 공백) 으로 제어됩니다.

4. **그리드 및 범례**:
   - 그리드는 시청자가 차트에서 값을 더 정확하게 읽는 데 도움이 됩니다.
   - 범례는 색상 선의 의미를 설명합니다.

## 텍스트 상자 배치에 대한 최종 참고 사항

시각화에 여러 텍스트 요소를 배치할 때는 다음 사항을 고려하십시오.

1. **시각적 계층 구조**: 가장 중요한 정보가 가장 눈에 띄어야 합니다.
2. **위치 지정**: 관련 정보를 시각화의 관련 부분 근처에 배치합니다.
3. **대비**: 텍스트가 배경에 대해 읽을 수 있는지 확인합니다.
4. **일관성**: 유사한 유형의 정보에 대해 일관된 스타일을 사용합니다.
5. **혼잡**: 너무 많은 텍스트 요소로 시각화를 과도하게 채우지 않도록 합니다.

텍스트 상자를 신중하게 배치하고 스타일을 지정하면 정보 제공과 시각적 매력을 모두 갖춘 시각화를 만들어 데이터에서 주요 통찰력을 이해하도록 시청자를 안내할 수 있습니다.
