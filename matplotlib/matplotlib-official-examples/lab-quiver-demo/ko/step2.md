# 피벗 포인트 (Pivot Point) 및 화살표 빈도

`quiver()` 함수는 화살표의 피벗 포인트와 화살표가 표시되는 빈도를 사용자 정의하는 데에도 사용할 수 있습니다. `pivot` 매개변수는 `'mid'` 또는 `'tip'`으로 설정할 수 있으며, `quiver()`에 전달된 배열을 슬라이싱하여 n 번째 화살표만 표시할 수 있습니다.

```python
fig2, ax2 = plt.subplots()
ax2.set_title("pivot='mid'; every third arrow; units='inches'")
Q = ax2.quiver(X[::3, ::3], Y[::3, ::3], U[::3, ::3], V[::3, ::3],
               pivot='mid', units='inches')
qk = ax2.quiverkey(Q, 0.9, 0.9, 1, r'$1 \frac{m}{s}$', labelpos='E',
                   coordinates='figure')
ax2.scatter(X[::3, ::3], Y[::3, ::3], color='r', s=5)
plt.show()
```
