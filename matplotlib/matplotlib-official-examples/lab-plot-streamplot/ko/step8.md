# 끊어지지 않은 Streamline

이 단계에서는 끊어지지 않은 streamline 을 사용하여 streamplot 을 생성합니다. `broken_streamlines` 매개변수는 단일 그리드 셀 내의 선의 한계를 초과할 때 streamline 을 끊을지 여부를 제어합니다.

```python
plt.streamplot(X, Y, U, V, broken_streamlines=False)
plt.title('Streamplot with Unbroken Streamlines')
plt.show()
```
