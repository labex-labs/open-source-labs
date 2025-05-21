# 달러 기호로 Y 축 레이블 서식 지정

이제 기본 플롯이 준비되었으므로, y 축 레이블의 서식을 지정하여 달러 기호를 표시해 보겠습니다. 이렇게 하면 금융 데이터를 더 읽기 쉽고 전문적으로 표현할 수 있습니다.

y 축의 눈금 레이블 서식을 지정하기 위해 Matplotlib 의 `ticker` 모듈을 사용합니다. 이 모듈은 다양한 서식 옵션을 제공합니다. 특히, `StrMethodFormatter` 클래스를 사용하여 y 축에 대한 사용자 지정 formatter 를 생성합니다.

노트북의 새 셀에 다음 코드를 추가하고 실행합니다.

```python
# Import the necessary module for formatting
import matplotlib.ticker as ticker

# Create a figure and axes
fig, ax = plt.subplots(figsize=(10, 6))

# Plot the daily revenue data
ax.plot(days, daily_revenue, marker='o', linestyle='-', color='blue', linewidth=2, markersize=6)

# Format y-axis with dollar signs
formatter = ticker.StrMethodFormatter('${x:,.2f}')
ax.yaxis.set_major_formatter(formatter)

# Add labels and title
ax.set_xlabel('Day', fontsize=12)
ax.set_ylabel('Revenue ($)', fontsize=12)
ax.set_title('Daily Revenue Over 30 Days', fontsize=14, fontweight='bold')

# Add grid for better readability
ax.grid(True, linestyle='--', alpha=0.7)

# Display the plot
plt.tight_layout()
plt.show()

print("Plot with dollar-formatted y-axis created!")
```

이 코드를 실행하면 y 축 레이블에 달러 기호가 있는 새 플롯이 표시됩니다.

이 코드의 핵심 부분을 설명해 보겠습니다.

```python
formatter = ticker.StrMethodFormatter('${x:,.2f}')
ax.yaxis.set_major_formatter(formatter)
```

다음은 이 서식 문자열이 수행하는 작업입니다.

- `$` - 각 레이블의 시작 부분에 달러 기호를 추가합니다.
- `{x:,.2f}` - 다음을 사용하여 숫자의 서식을 지정합니다.
  - `,` - 천 단위 구분 기호로 쉼표를 사용합니다 (예: 1000 대신 1,000).
  - `.2f` - 소수점 두 자리 (예: $1,234.56).

이 formatter 는 y 축의 모든 주요 눈금 레이블에 적용됩니다. 이제 플롯이 값이 달러로 표시됨을 명확하게 나타내어 금융 데이터 시각화에 훨씬 더 적합하게 되었음을 확인하십시오.
