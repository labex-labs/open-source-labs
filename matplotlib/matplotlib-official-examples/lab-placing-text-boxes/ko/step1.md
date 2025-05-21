# Jupyter Notebook 생성 및 데이터 준비

이 첫 번째 단계에서는 새로운 Jupyter Notebook 을 생성하고 시각화를 위한 데이터를 설정합니다.

## 새로운 Notebook 생성

Notebook 의 첫 번째 셀에서 필요한 라이브러리를 가져오겠습니다. 다음 코드를 입력하고 "Run" 버튼을 클릭하거나 Shift+Enter 를 눌러 실행합니다.

```python
import matplotlib.pyplot as plt
import numpy as np
```

![libraries-imported](../assets/screenshot-20250306-Azb1cb3S@2x.png)

이 코드는 두 가지 필수 라이브러리를 가져옵니다.

- `matplotlib.pyplot`: matplotlib 을 MATLAB 처럼 작동하게 해주는 함수의 모음
- `numpy`: Python 에서 과학적 계산을 위한 기본 패키지

## 샘플 데이터 생성

이제 시각화할 샘플 데이터를 생성해 보겠습니다. 새 셀에 다음 코드를 입력하고 실행합니다.

```python
# Set a random seed for reproducibility
np.random.seed(19680801)

# Generate 10,000 random numbers from a normal distribution
x = 30 * np.random.randn(10000)

# Calculate basic statistics
mu = x.mean()
median = np.median(x)
sigma = x.std()

# Display the statistics
print(f"Mean (μ): {mu:.2f}")
print(f"Median: {median:.2f}")
print(f"Standard Deviation (σ): {sigma:.2f}")
```

이 셀을 실행하면 다음과 유사한 출력이 표시됩니다.

```
Mean (μ): -0.31
Median: -0.28
Standard Deviation (σ): 29.86
```

정확한 값은 약간 다를 수 있습니다. 정규 분포에서 생성된 10,000 개의 난수로 데이터 세트를 생성하고 세 가지 중요한 통계를 계산했습니다.

1. 평균 (μ): 모든 데이터 포인트의 평균값
2. 중앙값: 데이터를 정렬했을 때 중간값
3. 표준 편차 (σ): 데이터가 얼마나 퍼져 있는지 측정하는 척도

이러한 통계는 나중에 시각화에 주석을 추가하는 데 사용됩니다.
