# 枢軸点と矢印の頻度

`quiver()`関数を使用すると、矢印の枢軸点と表示頻度をカスタマイズすることもできます。`pivot`パラメータを`'mid'`または`'tip'`に設定し、`quiver()`に渡される配列をスライスして、n 番目の矢印のみを表示することができます。

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
