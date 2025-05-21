# 기본 금융 플롯 생성

이제 데이터를 준비했으니, 일일 수익을 시각화하기 위한 기본 플롯을 생성해 보겠습니다. 30 일 기간 동안의 수익 추세를 보여주는 간단한 선 그래프로 시작합니다.

노트북의 새 셀에 다음 코드를 추가하고 실행합니다.

```python
# Create a figure and axes
fig, ax = plt.subplots(figsize=(10, 6))

# Plot the daily revenue data
ax.plot(days, daily_revenue, marker='o', linestyle='-', color='blue', linewidth=2, markersize=6)

# Add labels and title
ax.set_xlabel('Day', fontsize=12)
ax.set_ylabel('Revenue', fontsize=12)
ax.set_title('Daily Revenue Over 30 Days', fontsize=14, fontweight='bold')

# Add grid for better readability
ax.grid(True, linestyle='--', alpha=0.7)

# Display the plot
plt.tight_layout()
plt.show()

print("Basic plot created successfully!")
```

이 코드를 실행하면 일일 수익 추세를 보여주는 선 그래프가 표시됩니다. 다음과 유사하게 보일 것입니다 (실제 값은 무작위 생성으로 인해 약간 다를 수 있습니다).

![Basic Revenue Plot](../assets/screenshot-20250306-ywFsL4VH@2x.png)

이 코드에서 수행한 작업을 자세히 살펴보겠습니다.

1. `fig, ax = plt.subplots(figsize=(10, 6))` - 10×6 인치 크기의 figure 와 axes 를 생성했습니다.
2. `ax.plot(days, daily_revenue, ...)` - x 축에 날짜, y 축에 수익을 사용하여 데이터를 플롯했습니다.
3. `ax.set_xlabel()`, `ax.set_ylabel()`, `ax.set_title()` - 플롯에 레이블과 제목을 추가했습니다.
4. `ax.grid()` - 데이터를 더 쉽게 읽을 수 있도록 그리드를 추가했습니다.
5. `plt.tight_layout()` - 모든 것이 잘 맞도록 패딩을 조정했습니다.
6. `plt.show()` - 플롯을 표시했습니다.

현재 y 축에는 달러 기호 없이 일반 숫자가 표시되어 있습니다. 다음 단계에서는 y 축에 적절한 통화 형식을 표시하도록 플롯을 수정합니다.
