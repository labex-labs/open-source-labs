# 결과 시각화

마지막으로, 등장값 회귀 모델의 결과를 시각화해 보겠습니다. 원본 데이터 포인트를 산점도로, 예측 값을 선으로 표시할 수 있습니다.

```python
import matplotlib.pyplot as plt

# 원본 데이터와 예측 값을 플롯
plt.scatter(X, y, c='b', label='Original Data')
plt.plot(X_new, y_pred, c='r', label='Isotonic Regression')
plt.xlabel('X')
plt.ylabel('y')
plt.legend()
plt.show()
```
