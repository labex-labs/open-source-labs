# 바코드 렌더링

마지막으로, `Axes.imshow`를 사용하여 바코드를 렌더링할 수 있습니다. 데이터를 하나의 행을 가진 2D 배열로 변환하기 위해 `code.reshape(1, -1)`를 사용하고, 정사각형이 아닌 픽셀을 허용하기 위해 `imshow(..., aspect='auto')`를 사용하며, 흐릿한 가장자리를 방지하기 위해 `imshow(..., interpolation='nearest')`를 사용합니다.

```python
ax.imshow(code.reshape(1, -1), cmap='binary', aspect='auto',
          interpolation='nearest')
plt.show()
```
