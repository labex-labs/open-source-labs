# Создать второй график

Далее мы создадим второй график. Мы снова используем `subplot`, но на этот раз мы установим атрибут `sharex` для первого графика (`ax1`). Это гарантирует, что второй график будет иметь ту же ось X, что и первый график.

```python
ax2 = plt.subplot(212, sharex=ax1)
ax2.plot(t, np.sin(4*np.pi*t))
```
