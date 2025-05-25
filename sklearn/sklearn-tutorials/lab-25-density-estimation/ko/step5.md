# 밀도 추정 시각화

마지막으로, 히스토그램과 추정된 밀도 함수를 사용하여 밀도 추정 결과를 시각화할 수 있습니다. 원본 데이터의 히스토그램과 추정된 밀도 함수를 모두 플롯할 수 있습니다.

```python
import matplotlib.pyplot as plt

bins = np.linspace(-5, 5, 50)
plt.hist(X, bins=bins, density=True, alpha=0.5, label='Histogram')
plt.plot(X, np.exp(scores), color='red', label='Kernel Density Estimate')
plt.legend()
plt.show()
```
