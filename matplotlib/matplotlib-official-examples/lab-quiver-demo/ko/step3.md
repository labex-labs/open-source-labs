# X 뷰 (View) 에 따른 화살표 크기 조정

`quiver()` 함수는 또한 x 뷰에 따라 화살표 크기를 조정할 수 있도록 합니다. 이는 데이터에 따라 다른 크기로 화살표를 표시하는 데 유용할 수 있습니다.

```python
fig3, ax3 = plt.subplots()
ax3.set_title("pivot='tip'; scales with x view")
M = np.hypot(U, V)
Q = ax3.quiver(X, Y, U, V, M, units='x', pivot='tip', width=0.022,
               scale=1 / 0.15)
qk = ax3.quiverkey(Q, 0.9, 0.9, 1, r'$1 \frac{m}{s}$', labelpos='E',
                   coordinates='figure')
ax3.scatter(X, Y, color='0.5', s=1)
plt.show()
```
