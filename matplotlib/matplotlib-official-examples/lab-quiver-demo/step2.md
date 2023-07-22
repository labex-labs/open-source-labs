# Pivot Point and Arrow Frequency

The `quiver()` function can also be used to customize the pivot point of the arrows and the frequency at which they are displayed. The `pivot` parameter can be set to `'mid'` or `'tip'`, and the arrays passed to `quiver()` can be sliced to display only every nth arrow.

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
