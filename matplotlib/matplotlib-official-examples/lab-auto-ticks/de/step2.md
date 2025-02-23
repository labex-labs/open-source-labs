# Streudiagramm mit autolimit_mode 'round_numbers'

In diesem Schritt werden wir die `axes.autolimit_mode` auf 'round_numbers' umschalten und ein Streudiagramm erstellen, um Tick-Marks an geraden Zahlen zu halten und auch Tick-Marks an den Rändern zu haben.

```python
plt.rcParams['axes.autolimit_mode'] = 'round_numbers'

fig, ax = plt.subplots()
ax.scatter(x, y, c=x+y)
plt.show()
```
