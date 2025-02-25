# Масштабирование стрелок по оси X

Функция `quiver()` также позволяет масштабировать стрелки в зависимости от вида по оси X. Это может быть полезно для отображения стрелок в разных масштабах в зависимости от данных.

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
