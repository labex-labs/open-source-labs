# 그리드 생성

이제 그래프에 표시할 그리드를 생성합니다. 그리드는 그리드 상의 각 점에 대한 예측 확률을 표시하는 데 사용됩니다. 또한 메쉬의 간격 크기를 정의합니다.

```python
h = 0.02  # 메쉬의 간격 크기

x_min, x_max = X[:, 0].min() - 1, X[:, 0].max() + 1
y_min, y_max = X[:, 1].min() - 1, X[:, 1].max() + 1
xx, yy = np.meshgrid(np.arange(x_min, x_max, h), np.arange(y_min, y_max, h))
```
