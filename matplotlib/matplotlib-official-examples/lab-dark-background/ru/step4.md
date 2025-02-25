# Строим график данных

В этом шаге мы построим график с примерными данными, сгенерированными на предыдущем шаге. Мы будем использовать цикл `for`, чтобы построить несколько синусоидальных волн с разными фазами.

```python
fig, ax = plt.subplots()

ncolors = len(plt.rcParams['axes.prop_cycle'])
shift = np.linspace(0, L, ncolors, endpoint=False)

for s in shift:
    # Plot the sine wave with a phase shift of s
    ax.plot(x, np.sin(x + s), 'o-')

ax.set_xlabel('x-axis')
ax.set_ylabel('y-axis')
ax.set_title("'dark_background' style sheet")

plt.show()
```
