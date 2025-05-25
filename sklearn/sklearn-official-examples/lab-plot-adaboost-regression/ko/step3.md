# 결과 플롯

마지막으로, 단일 의사결정 트리 회귀자와 AdaBoost 회귀자라는 두 회귀자가 데이터에 얼마나 잘 맞는지 플롯합니다. Matplotlib 의 `scatter()` 함수를 사용하여 학습 샘플과 두 회귀자의 예측 값을 플롯합니다. Matplotlib 의 `plot()` 함수를 사용하여 두 회귀자 모두에 대해 데이터에 대한 예측 값을 플롯합니다. 플롯에 범례를 추가하여 두 회귀자를 구분합니다.

```python
import matplotlib.pyplot as plt
import seaborn as sns

colors = sns.color_palette("colorblind")

plt.figure()
plt.scatter(X, y, color=colors[0], label="training samples")
plt.plot(X, y_1, color=colors[1], label="n_estimators=1", linewidth=2)
plt.plot(X, y_2, color=colors[2], label="n_estimators=300", linewidth=2)
plt.xlabel("데이터")
plt.ylabel("대상")
plt.title("부스팅된 의사결정 트리 회귀")
plt.legend()
plt.show()
```
