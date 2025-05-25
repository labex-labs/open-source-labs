# 결과 플롯

모델이 데이터에 얼마나 잘 맞는지 시각화하기 위해 결과를 플롯합니다.

```python
plt.figure()
plt.scatter(X, y, s=20, edgecolor="black", c="darkorange", label="data")
plt.plot(X_test, y_1, color="cornflowerblue", label="max_depth=2", linewidth=2)
plt.plot(X_test, y_2, color="yellowgreen", label="max_depth=5", linewidth=2)
plt.xlabel("데이터")
plt.ylabel("타겟")
plt.title("결정 트리 회귀")
plt.legend()
plt.show()
```
