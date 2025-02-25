# Punto de pivote y frecuencia de las flechas

La función `quiver()` también se puede utilizar para personalizar el punto de pivote de las flechas y la frecuencia con la que se muestran. El parámetro `pivot` se puede establecer en `'mid'` o `'tip'`, y los arrays pasados a `quiver()` se pueden segmentar para mostrar solo cada n-ésima flecha.

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
