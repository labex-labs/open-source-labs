# 환경 준비 및 데이터 생성

이 첫 번째 단계에서는 필요한 라이브러리를 가져오고 시각화를 위한 샘플 데이터를 생성하여 작업 환경을 설정합니다. 끊어진 축 플롯의 가치를 보여주기 위해 이상치를 포함하는 데이터를 생성하는 데 중점을 둡니다.

## 필요한 라이브러리 가져오기

이 튜토리얼에 필요한 라이브러리를 가져오는 것으로 시작해 보겠습니다. 시각화를 위해 Matplotlib 을 사용하고, 숫자 데이터를 생성하고 조작하기 위해 NumPy 를 사용합니다.

Jupyter Notebook 에서 새 셀을 만들고 다음 코드를 입력합니다.

```python
import matplotlib.pyplot as plt
import numpy as np

print(f"NumPy version: {np.__version__}")
```

이 셀을 실행하면 다음과 유사한 출력이 표시됩니다.

```
NumPy version: 2.0.0
```

![numpy-version](../assets/screenshot-20250306-Um0MaTKw@2x.png)

정확한 버전 번호는 환경에 따라 다를 수 있지만, 이는 라이브러리가 제대로 설치되어 사용할 준비가 되었음을 확인합니다.

## 이상치를 포함하는 샘플 데이터 생성

이제 이상치를 포함하는 샘플 데이터 세트를 생성해 보겠습니다. 무작위 숫자를 생성한 다음, 특정 위치에 의도적으로 더 큰 값을 추가하여 이상치를 만듭니다.

새 셀을 만들고 다음 코드를 추가합니다.

```python
# Set random seed for reproducibility
np.random.seed(19680801)

# Generate 30 random points with values between 0 and 0.2
pts = np.random.rand(30) * 0.2

# Add 0.8 to two specific points to create outliers
pts[[3, 14]] += 0.8

# Display the first few data points to understand our dataset
print("First 10 data points:")
print(pts[:10])
print("\nData points containing outliers:")
print(pts[[3, 14]])
```

이 셀을 실행하면 다음과 유사한 출력이 표시됩니다.

```
First 10 data points:
[0.01182225 0.11765474 0.07404329 0.91088185 0.10502995 0.11190702
 0.14047499 0.01060192 0.15226977 0.06145634]

Data points containing outliers:
[0.91088185 0.97360754]
```

이 출력에서 인덱스 3 과 14 의 값이 다른 값보다 훨씬 크다는 것을 명확하게 볼 수 있습니다. 이것이 바로 이상치입니다. 대부분의 데이터 포인트는 0.2 미만이지만, 이 두 개의 이상치는 0.9 이상으로, 데이터 세트에 상당한 불균형을 만듭니다.

이러한 종류의 데이터 분포는 끊어진 축 플롯의 유용성을 보여주기에 완벽합니다. 다음 단계에서는 플롯 구조를 만들고 주 데이터와 이상치를 모두 제대로 표시하도록 구성합니다.
