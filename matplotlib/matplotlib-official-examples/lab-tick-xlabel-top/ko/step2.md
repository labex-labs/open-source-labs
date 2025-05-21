# 기본 설정을 사용하여 기본 플롯 생성

이제 Matplotlib 를 가져왔으므로 기본 설정을 사용하여 간단한 플롯을 생성하여 축과 눈금 레이블이 기본적으로 어떻게 배치되는지 이해해 보겠습니다.

## Matplotlib 구성 요소 이해

Matplotlib 에서 플롯은 여러 구성 요소로 구성됩니다.

- **Figure (그림)**: 플롯의 전체 컨테이너
- **Axes (축)**: 자체 좌표계를 사용하여 데이터가 플롯되는 영역
- **Axis (축)**: 좌표계를 정의하는 숫자선과 같은 객체
- **Ticks (눈금)**: 특정 값을 나타내는 축의 표시
- **Tick Labels (눈금 레이블)**: 각 눈금의 값을 나타내는 텍스트 레이블

기본적으로 x 축 눈금 레이블은 플롯 하단에 나타납니다.

## 간단한 플롯 생성

Notebook 의 새 셀에서 간단한 선 플롯을 생성해 보겠습니다.

```python
# Create a figure and a set of axes
fig, ax = plt.subplots(figsize=(8, 5))

# Generate some data
x = np.arange(0, 10, 1)
y = np.sin(x)

# Plot the data
ax.plot(x, y, marker='o', linestyle='-', color='blue', label='sin(x)')

# Add a title and labels
ax.set_title('A Simple Sine Wave Plot')
ax.set_xlabel('X-axis')
ax.set_ylabel('Y-axis (sin(x))')

# Add a grid and legend
ax.grid(True, linestyle='--', alpha=0.7)
ax.legend()

# Display the plot
plt.show()

print("Notice that the x-axis tick labels are at the bottom of the plot by default.")
```

이 코드를 실행하면 Matplotlib 의 기본 위치인 플롯 하단에 x 축 눈금 레이블이 있는 사인파 플롯이 표시됩니다.

플롯이 어떻게 구성되어 있는지, 눈금 레이블이 어디에 배치되어 있는지 잠시 살펴보십시오. 이 이해는 다음 단계에서 변경할 사항을 이해하는 데 도움이 됩니다.
