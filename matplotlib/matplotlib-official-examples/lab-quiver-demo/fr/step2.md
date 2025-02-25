# Point de pivot et fréquence des flèches

La fonction `quiver()` peut également être utilisée pour personnaliser le point de pivot des flèches et la fréquence à laquelle elles sont affichées. Le paramètre `pivot` peut être défini sur `'mid'` ou `'tip'`, et les tableaux passés à `quiver()` peuvent être coupés pour n'afficher qu'une flèche sur n.

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
