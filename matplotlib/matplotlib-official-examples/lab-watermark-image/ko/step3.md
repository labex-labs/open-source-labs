# 임의 데이터를 사용한 기본 플롯 생성

이미지 오버레이를 추가하기 전에 시각화의 기반이 될 플롯을 만들어야 합니다. 임의 데이터를 사용하여 간단한 막대 차트를 만들어 보겠습니다.

1. 노트북에 새 셀을 만들고 다음 코드를 입력합니다.

```python
# Create a figure and axes for our plot
fig, ax = plt.subplots(figsize=(10, 6))

# Set a random seed for reproducibility
np.random.seed(19680801)

# Generate random data
x = np.arange(30)  # x-axis values (0 to 29)
y = x + np.random.randn(30)  # y-axis values (x plus random noise)

# Create a bar chart
bars = ax.bar(x, y, color='#6bbc6b')  # Green bars

# Add grid lines
ax.grid(linestyle='--', alpha=0.7)

# Add labels and title
ax.set_xlabel('X-axis Label')
ax.set_ylabel('Y-axis Label')
ax.set_title('Bar Chart with Random Data')

# Display the plot
plt.tight_layout()
plt.show()
```

이 코드는 다음을 수행합니다.

- `plt.subplots()`를 사용하여 특정 크기의 figure 와 axes 를 생성합니다.
- 코드를 실행할 때마다 동일한 임의 값을 얻을 수 있도록 임의 시드를 설정합니다.
- 30 개의 x 값 (0 에서 29 까지) 과 해당 y 값 (x + 임의 노이즈) 을 생성합니다.
- `ax.bar()`를 사용하여 녹색 막대가 있는 막대 차트를 생성합니다.
- `ax.grid()`를 사용하여 플롯에 격자선을 추가합니다.
- x 축, y 축 레이블과 플롯 제목을 추가합니다.
- `plt.tight_layout()`을 사용하여 모양을 개선하기 위해 간격을 조정합니다.
- `plt.show()`를 사용하여 플롯을 표시합니다.

2. Shift+Enter 를 눌러 셀을 실행합니다.

출력은 임의 데이터를 나타내는 녹색 막대가 있는 막대 차트를 표시해야 합니다. x 축은 0 에서 29 까지의 정수를 표시하고 y 축은 임의 노이즈가 추가된 해당 값을 표시합니다.

이 플롯은 다음 단계에서 이미지를 오버레이할 기반이 됩니다. figure 객체를 변수 `fig`에, axes 객체를 변수 `ax`에 저장했음을 확인하십시오. 이미지 오버레이를 추가하려면 이러한 변수가 필요합니다.
