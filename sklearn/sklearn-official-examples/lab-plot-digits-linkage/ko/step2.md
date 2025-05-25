# 데이터셋 로드 및 준비

숫자 데이터셋을 로드하고 데이터와 대상 레이블을 추출하여 군집화를 위한 준비를 합니다. 또한 재현성을 보장하기 위해 난수 시드를 0 으로 설정합니다.

```python
digits = datasets.load_digits()
X, y = digits.data, digits.target
n_samples, n_features = X.shape
np.random.seed(0)
```
