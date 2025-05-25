# 데이터 생성

훈련, 테스트 및 이상치 데이터를 생성하기 위해 numpy 를 사용합니다. 100 개의 정상 훈련 관측치, 20 개의 정상 테스트 관측치 및 20 개의 비정상 신규 관측치를 생성합니다.

```python
np.random.seed(42)

xx, yy = np.meshgrid(np.linspace(-5, 5, 500), np.linspace(-5, 5, 500))
X = 0.3 * np.random.randn(100, 2)
X_train = np.r_[X + 2, X - 2]
X = 0.3 * np.random.randn(20, 2)
X_test = np.r_[X + 2, X - 2]
X_outliers = np.random.uniform(low=-4, high=4, size=(20, 2))
```
