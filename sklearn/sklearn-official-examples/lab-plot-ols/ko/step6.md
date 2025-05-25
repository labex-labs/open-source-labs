# 결과 시각화

마지막으로, 예측 값과 실제 값을 플롯하여 모델이 데이터에 얼마나 잘 맞는지 시각적으로 확인할 수 있습니다.

```python
import matplotlib.pyplot as plt

# 출력 플롯
plt.scatter(diabetes_X_test, diabetes_y_test, color="black")
plt.plot(diabetes_X_test, diabetes_y_pred, color="blue", linewidth=3)

plt.xticks(())
plt.yticks(())

plt.show()
```
