# 선 너비 변화

이 단계에서는 선 너비가 변하는 streamplot 을 생성합니다. `linewidth` 매개변수는 streamline 의 너비를 제어합니다. 여기서는 앞서 계산한 `speed` 배열을 사용하여 선 너비를 변경합니다.

```python
lw = 5*speed / speed.max()
plt.streamplot(X, Y, U, V, density=0.6, color='k', linewidth=lw)
plt.title('Varying Line Width')
plt.show()
```
