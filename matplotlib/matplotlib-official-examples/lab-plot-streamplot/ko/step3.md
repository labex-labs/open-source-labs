# 밀도 변화

이 단계에서는 밀도가 변하는 streamplot 을 생성합니다. `density` 매개변수는 플롯할 streamline 의 수를 제어합니다. 값이 높을수록 더 많은 streamline 이 생성됩니다.

```python
plt.streamplot(X, Y, U, V, density=[0.5, 1])
plt.title('Varying Density')
plt.show()
```
