# Построить график данных

Теперь мы можем построить график наших данных с использованием функции `plot`. Мы создадим две линии с использованием данных, созданных на шаге 3.

```python
ax.plot(theta, r, color="tab:orange", lw=3, label="a line")
ax.plot(0.5 * theta, r, color="tab:blue", ls="--", lw=3, label="another line")
```
