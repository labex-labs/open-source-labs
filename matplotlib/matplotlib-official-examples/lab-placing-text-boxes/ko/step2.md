# 기본 히스토그램 생성

이제 데이터를 확보했으므로, 분포를 시각화하기 위해 히스토그램을 생성해 보겠습니다. 히스토그램은 데이터를 빈 (bin, 범위) 으로 나누고 각 빈 내의 데이터 포인트 빈도를 표시합니다.

## 히스토그램 생성

Jupyter Notebook 의 새 셀에 다음 코드를 입력하고 실행합니다.

```python
# Create a figure and axes
fig, ax = plt.subplots(figsize=(10, 6))

# Create a histogram with 50 bins
histogram = ax.hist(x, bins=50, color='skyblue', edgecolor='black')

# Add title and labels
ax.set_title('Distribution of Random Data', fontsize=16)
ax.set_xlabel('Value', fontsize=12)
ax.set_ylabel('Frequency', fontsize=12)

# Display the plot
plt.tight_layout()
plt.show()
```

이 셀을 실행하면 무작위 데이터의 분포를 표시하는 히스토그램이 표시됩니다. 출력은 0 근처에 중심을 둔 종 모양 곡선 (정규 분포) 처럼 보일 것입니다.

## 코드 이해

코드의 각 줄이 수행하는 작업을 자세히 살펴보겠습니다.

1. `fig, ax = plt.subplots(figsize=(10, 6))`: figure 및 axes 객체를 생성합니다. `figsize` 매개변수는 플롯의 크기를 인치 단위로 설정합니다 (너비, 높이).

2. `histogram = ax.hist(x, bins=50, color='skyblue', edgecolor='black')`: 50 개의 빈으로 데이터 `x`의 히스토그램을 생성합니다. 빈은 하늘색으로 칠해지고 검은색 테두리가 있습니다.

3. `ax.set_title('Distribution of Random Data', fontsize=16)`: 글꼴 크기가 16 인 플롯에 제목을 추가합니다.

4. `ax.set_xlabel('Value', fontsize=12)` 및 `ax.set_ylabel('Frequency', fontsize=12)`: 글꼴 크기가 12 인 x 및 y 축에 레이블을 추가합니다.

5. `plt.tight_layout()`: 플롯이 figure 영역에 맞게 자동으로 조정됩니다.

6. `plt.show()`: 플롯을 표시합니다.

히스토그램은 데이터가 어떻게 분포되어 있는지 보여줍니다. 정규 분포에서 데이터를 생성하는 `np.random.randn()`을 사용했으므로 히스토그램은 0 을 중심으로 하는 종 모양을 갖습니다. 각 막대의 높이는 해당 범위 내에 속하는 데이터 포인트의 수를 나타냅니다.
