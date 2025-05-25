# 최적화된 예측 함수 시각화

마지막으로, 최적화된 하이퍼파라미터를 사용하여 예측 함수를 시각화해 보겠습니다.

```python
# 최적화된 모델을 사용하여 타겟 값 예측
y_pred_opt = best_krr.predict(X_test)

# 데이터와 최적화된 예측 함수 시각화
plt.scatter(X, y, color='blue', label='Data')
plt.plot(X_test, y_pred_opt, color='green', label='Optimized Predicted Function')
plt.xlabel('X')
plt.ylabel('y')
plt.legend()
plt.show()
```
