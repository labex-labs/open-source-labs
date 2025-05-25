# 색상 변화

이 단계에서는 색상이 변하는 streamplot 을 생성합니다. `color` 매개변수는 벡터 필드의 크기를 나타내는 2D 배열을 사용합니다. 여기서는 벡터 필드의 `U` 구성 요소를 색상으로 사용합니다.

```python
strm = plt.streamplot(X, Y, U, V, color=U, linewidth=2, cmap='autumn')
plt.colorbar(strm.lines)
plt.title('Varying Color')
plt.show()
```
