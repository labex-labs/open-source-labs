# Сравнение масштабирования "symlog" и "asinh" для двумерных случайных чисел, распределенных по Коши

Наконец, мы сравним масштабирование "symlog" и "asinh" для двумерных случайных чисел, распределенных по Коши. Мы построим один и тот же график дважды, один раз с использованием "symlog", а другой раз с использованием "asinh".

```python
fig3 = plt.figure()
ax = fig3.subplots(1, 1)
r = 3 * np.tan(np.random.uniform(-np.pi / 2.02, np.pi / 2.02,
                                 size=(5000,)))
th = np.random.uniform(0, 2*np.pi, size=r.shape)

ax.scatter(r * np.cos(th), r * np.sin(th), s=4, alpha=0.5)
ax.set_xscale('asinh')
ax.set_yscale('symlog')
ax.set_xlabel('asinh')
ax.set_ylabel('symlog')
ax.set_title('2D Cauchy random deviates')
ax.set_xlim(-50, 50)
ax.set_ylim(-50, 50)
ax.grid()
```
