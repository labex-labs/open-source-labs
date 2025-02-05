# 可视化预测函数

模型训练完成后，让我们将预测函数与原始数据点一起可视化。

```python
# 生成测试数据点
X_test = np.linspace(0, 5, 100)[:, None]

# 预测目标值
y_pred = krr.predict(X_test)

# 可视化数据和预测函数
plt.scatter(X, y, color='blue', label='Data')
plt.plot(X_test, y_pred, color='red', label='Predicted Function')
plt.xlabel('X')
plt.ylabel('y')
plt.legend()
plt.show()
```
