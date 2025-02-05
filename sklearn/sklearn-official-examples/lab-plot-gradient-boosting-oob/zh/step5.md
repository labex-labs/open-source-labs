# 绘制结果

最后，我们可以绘制结果，以直观展示模型在不同迭代次数下的性能。我们将在 y 轴上绘制负对数损失，在 x 轴上绘制迭代次数。

```python
plt.figure(figsize=(10, 5))
plt.plot(range(1, params['n_estimators'] + 1), cv_scores, label='CV')
plt.plot(range(1, params['n_estimators'] + 1), test_scores, label='Test')
plt.axvline(x=best_n_estimators, color='red', linestyle='--')
plt.xlabel('Number of iterations')
plt.ylabel('Negative log-loss')
plt.legend()
plt.show()
```
