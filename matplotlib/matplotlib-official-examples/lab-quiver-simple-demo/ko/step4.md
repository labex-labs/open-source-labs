# Quiver Key 생성

화살표의 크기를 표시하기 위해 plot 에 quiver key 를 추가할 수 있습니다. `ax.quiverkey()` 함수를 사용하여 key 를 추가합니다. `q` 객체, key 의 `X` 및 `Y` 위치, 화살표의 길이, key 의 레이블, 그리고 레이블의 위치를 전달합니다.

```python
ax.quiverkey(q, X=0.3, Y=1.1, U=10,
             label='Quiver key, length = 10', labelpos='E')
```
