# Визуализируем оптимизированную предсказанную функцию

Наконец, давайте визуализируем предсказанную функцию с использованием оптимизированных гиперпараметров.

```python
# Predict the target values using the optimized model
y_pred_opt = best_krr.predict(X_test)

# Visualize the data and the optimized predicted function
plt.scatter(X, y, color='blue', label='Data')
plt.plot(X_test, y_pred_opt, color='green', label='Optimized Predicted Function')
plt.xlabel('X')
plt.ylabel('y')
plt.legend()
plt.show()
```
