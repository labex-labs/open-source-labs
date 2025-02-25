# Создадим вторичную ось y

Создадим третий пример связывания осей в трансформации, которая является эмпирически полученной из данных и специфичной для них. В этом случае мы зададим функции прямых и обратных преобразований в виде линейной интерполяции из одного набора данных в другой.

```python
fig, ax = plt.subplots(layout='constrained')
xdata = np.arange(1, 11, 0.4)
ydata = np.random.randn(len(xdata))
ax.plot(xdata, ydata, label='Plotted data')

xold = np.arange(0, 11, 0.2)
# фальшивый набор данных, связывающий координату x с другой координатой, полученной из данных.
# xnew должен быть монотонным, поэтому мы сортируем...
xnew = np.sort(10 * np.exp(-xold / 4) + np.random.randn(len(xold)) / 3)

ax.plot(xold[3:], xnew[3:], label='Transform data')
ax.set_xlabel('X [m]')
ax.legend()

def forward(x):
    return np.interp(x, xold, xnew)

def inverse(x):
    return np.interp(x, xnew, xold)

secax = ax.secondary_xaxis('top', functions=(forward, inverse))
secax.xaxis.set_minor_locator(AutoMinorLocator())
secax.set_xlabel('$X_{other}$')
```
