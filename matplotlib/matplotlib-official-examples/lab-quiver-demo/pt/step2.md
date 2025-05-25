# Ponto de Pivô e Frequência das Setas

A função `quiver()` também pode ser usada para personalizar o ponto de pivô (pivot point) das setas e a frequência com que elas são exibidas. O parâmetro `pivot` pode ser definido como `'mid'` ou `'tip'`, e os arrays passados para `quiver()` podem ser fatiados (sliced) para exibir apenas a cada enésima seta.

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
