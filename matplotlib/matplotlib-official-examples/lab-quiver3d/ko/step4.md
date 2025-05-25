# Quiver 플롯 생성

그리드와 화살표의 방향이 정의되었으므로, quiver 플롯을 생성할 수 있습니다. 이 예제에서는 Matplotlib 의 `quiver` 함수를 사용하여 플롯을 생성합니다. `length` 매개변수는 화살표의 길이를 설정하고, `normalize` 매개변수는 화살표를 길이 1 로 정규화합니다.

```python
ax.quiver(x, y, z, u, v, w, length=0.1, normalize=True)
```
