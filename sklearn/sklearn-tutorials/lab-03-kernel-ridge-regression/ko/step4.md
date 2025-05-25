# 예측 함수 시각화

모델 학습이 완료되면 원본 데이터 포인트와 함께 예측 함수를 시각화해 봅니다.

```python
# 테스트 데이터 포인트 생성
X_test = np.linspace(0, 5, 100)[:, None]

# 타겟 값 예측
y_pred = krr.predict(X_test)

# 데이터와 예측 함수 시각화
plt.scatter(X, y, color='blue', label='Data')
plt.plot(X_test, y_pred, color='red', label='Predicted Function')
plt.xlabel('X')
plt.ylabel('y')
plt.legend()
plt.show()
```
