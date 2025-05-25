# 특징 중요도 평가

불순도 감소량 (MDI) 을 기반으로 특징 중요도를 평가합니다. 특징 중요도는 맞춰진 속성 `feature_importances_`에 의해 제공되며, 각 트리 내 불순도 감소량의 누적 평균과 표준 편차로 계산됩니다.

```python
import time
import matplotlib.pyplot as plt

start_time = time.time()
img_shape = data.images[0].shape
importances = forest.feature_importances_
elapsed_time = time.time() - start_time

print(f"Elapsed time to compute the importances: {elapsed_time:.3f} seconds")
imp_reshaped = importances.reshape(img_shape)
plt.matshow(imp_reshaped, cmap=plt.cm.hot)
plt.title("불순도 값을 사용한 픽셀 중요도")
plt.colorbar()
plt.show()
```
