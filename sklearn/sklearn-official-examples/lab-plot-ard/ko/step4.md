# 주변 로그 - 가능도 시각화

두 모델의 주변 로그 - 가능도를 시각화합니다.

```python
import numpy as np

ard_scores = -np.array(ard.scores_)
brr_scores = -np.array(brr.scores_)
plt.plot(ard_scores, color="navy", label="ARD")
plt.plot(brr_scores, color="red", label="BayesianRidge")
plt.ylabel("로그 - 가능도")
plt.xlabel("반복 횟수")
plt.xlim(1, 30)
plt.legend()
_ = plt.title("모델 로그 - 가능도")
```
