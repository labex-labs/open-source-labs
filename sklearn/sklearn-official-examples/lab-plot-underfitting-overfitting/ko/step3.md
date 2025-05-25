# 데이터 시각화

실제 함수와 생성된 샘플을 플롯합니다.

```python
plt.figure(figsize=(6, 4))
plt.plot(np.linspace(0, 1, 100), true_fun(np.linspace(0, 1, 100)), label="True function")
plt.scatter(X, y, edgecolor="b", s=20, label="Samples")
plt.xlabel("x")
plt.ylabel("y")
plt.legend(loc="best")
plt.show()
```
