# Сравнение поведения "symlog" и "asinh" на примере графика y=x

Мы сравним поведение "symlog" и "asinh" на примере графика y=x. Мы построим один и тот же график дважды, один раз с использованием "symlog", а другой раз с использованием "asinh".

```python
fig1 = plt.figure()
ax0, ax1 = fig1.subplots(1, 2, sharex=True)

ax0.plot(x, x)
ax0.set_yscale('symlog')
ax0.grid()
ax0.set_title('symlog')

ax1.plot(x, x)
ax1.set_yscale('asinh')
ax1.grid()
ax1.set_title('asinh')
```
