# 결과 플롯

마지막으로, 모델의 결과를 플롯하여 서로 어떻게 비교되는지 확인할 수 있습니다. 각 모델의 지원 (즉, 0 이 아닌 계수의 위치) 과 특징 중 하나의 시계열을 플롯할 것입니다.

```python
import matplotlib.pyplot as plt

fig = plt.figure(figsize=(8, 5))
plt.subplot(1, 2, 1)
plt.spy(coef_lasso_)
plt.xlabel("특징")
plt.ylabel("시간 (또는 작업)")
plt.text(10, 5, "Lasso")
plt.subplot(1, 2, 2)
plt.spy(coef_multi_task_lasso_)
plt.xlabel("특징")
plt.ylabel("시간 (또는 작업)")
plt.text(10, 5, "MultiTaskLasso")
fig.suptitle("계수의 0 이 아닌 위치")

feature_to_plot = 0
plt.figure()
lw = 2
plt.plot(coef[:, feature_to_plot], color="seagreen", linewidth=lw, label="Ground truth")
plt.plot(
    coef_lasso_[:, feature_to_plot], color="cornflowerblue", linewidth=lw, label="Lasso"
)
plt.plot(
    coef_multi_task_lasso_[:, feature_to_plot],
    color="gold",
    linewidth=lw,
    label="MultiTaskLasso",
)
plt.legend(loc="upper center")
plt.axis("tight")
plt.ylim([-1.1, 1.1])
plt.show()
```
