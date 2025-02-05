# 可视化优化后的预测函数

最后，让我们使用优化后的超参数来可视化预测函数。

```python
# 使用优化后的模型预测目标值
y_pred_opt = best_krr.predict(X_test)

# 可视化数据和优化后的预测函数
plt.scatter(X, y, color='blue', label='Data')
plt.plot(X_test, y_pred_opt, color='green', label='Optimized Predicted Function')
plt.xlabel('X')
plt.ylabel('y')
plt.legend()
plt.show()
```
