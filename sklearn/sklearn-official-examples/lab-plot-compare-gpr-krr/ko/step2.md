# 단순 선형 모델의 한계

릿지 모델을 적합하고, 이 모델의 예측을 우리 데이터셋에 대해 확인합니다.

```python
from sklearn.linear_model import Ridge
import matplotlib.pyplot as plt

ridge = Ridge().fit(training_data, training_noisy_target)

plt.plot(data, target, label="True signal", linewidth=2)
plt.scatter(
    training_data,
    training_noisy_target,
    color="black",
    label="Noisy measurements",
)
plt.plot(data, ridge.predict(data), label="Ridge regression")
plt.legend()
plt.xlabel("data")
plt.ylabel("target")
_ = plt.title("릿지와 같은 선형 모델의 한계")
```
