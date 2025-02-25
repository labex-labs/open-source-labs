# Mettre à l'échelle les flèches avec la vue en x

La fonction `quiver()` permet également de mettre à l'échelle les flèches avec la vue en x. Cela peut être utile pour afficher des flèches à différentes échelles en fonction des données.

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
