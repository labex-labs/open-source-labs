# Точка опоры и частота стрелок

Функция `quiver()` также позволяет настроить точку опоры стрелок и частоту их отображения. Параметр `pivot` можно установить в значение `'mid'` или `'tip'`, а массивы, передаваемые в `quiver()`, можно срезыровать, чтобы отображать только каждую n-ю стрелку.

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
