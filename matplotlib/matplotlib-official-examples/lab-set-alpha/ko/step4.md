# 알파 값으로 산점도 만들기

이 단계에서는 알파 값에 대한 지식을 적용하여 산점도를 만듭니다. 이는 투명도가 겹치는 점이 있는 산점도에서 데이터 밀도를 시각화하는 데 어떻게 도움이 되는지 보여줍니다.

## 새 셀 추가

도구 모음에서 "+" 버튼을 클릭하거나 명령 모드에서 "Esc"를 누른 다음 "b"를 눌러 Jupyter Notebook 에 새 셀을 추가합니다.

## 투명도를 사용하여 산점도 만들기

새 셀에 다음 코드를 입력하고 실행합니다.

```python
import matplotlib.pyplot as plt
import numpy as np

# Set a random seed for reproducibility
np.random.seed(19680801)

# Create a figure and an axes
fig, ax = plt.subplots(figsize=(10, 6))

# Create two clusters of points
cluster1_x = np.random.normal(0.3, 0.15, 500)
cluster1_y = np.random.normal(0.3, 0.15, 500)

cluster2_x = np.random.normal(0.7, 0.15, 500)
cluster2_y = np.random.normal(0.7, 0.15, 500)

# Combine the clusters
x = np.concatenate([cluster1_x, cluster2_x])
y = np.concatenate([cluster1_y, cluster2_y])

# Create a scatter plot with alpha=0.5
scatter = ax.scatter(x, y, s=30, c='blue', alpha=0.5)

# Add a title and labels
ax.set_title("Scatter Plot with Alpha=0.5 Showing Data Density")
ax.set_xlabel("X")
ax.set_ylabel("Y")

# Set axis limits
ax.set_xlim(0, 1)
ax.set_ylim(0, 1)

# Add a grid
ax.grid(True, linestyle='--', alpha=0.7)

# Show the plot
plt.show()
```

## 코드 및 출력 이해하기

코드를 실행한 후 두 개의 점 클러스터가 있는 산점도가 표시되어야 합니다. 각 점은 0.5 의 투명도 수준을 가지므로 점이 겹치는 부분을 볼 수 있습니다.

코드의 주요 부분을 분석해 보겠습니다.

1. `cluster1_x = np.random.normal(0.3, 0.15, 500)` - 평균 0.3, 표준 편차 0.15 인 정규 분포를 따르는 500 개의 임의 x 좌표를 생성합니다.

2. `cluster1_y = np.random.normal(0.3, 0.15, 500)` - 첫 번째 클러스터에 대해 500 개의 임의 y 좌표를 생성합니다.

3. `cluster2_x` 및 `cluster2_y` - 마찬가지로 (0.7, 0.7) 을 중심으로 하는 두 번째 클러스터에 대한 좌표를 생성합니다.

4. `ax.scatter(..., alpha=0.5)` - 50% 불투명도로 점이 있는 산점도를 만듭니다.

산점도에서 알파를 사용하면 다음과 같은 이점이 있습니다.

1. **밀도 시각화**: 많은 점이 겹치는 영역은 더 어둡게 나타나 데이터 밀도를 보여줍니다.

2. **과도한 플로팅 감소**: 투명도가 없으면 겹치는 점이 서로 완전히 숨겨집니다.

3. **패턴 인식**: 투명도는 데이터에서 클러스터와 패턴을 식별하는 데 도움이 됩니다.

더 많은 점이 겹치는 영역이 시각화에서 더 어둡게 나타나는 것을 확인하십시오. 이는 밀도 추정과 같은 추가 기술 없이 데이터 밀도를 시각화하는 강력한 방법입니다.
