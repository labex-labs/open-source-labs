# Автоматическое определение делений для основных и вторичных делений шкалы

```python
# Create data
t = np.arange(0.0, 100.0, 0.01)
s = np.sin(2 * np.pi * t) * np.exp(-t * 0.01)

# Plot the data
fig, ax = plt.subplots()
ax.plot(t, s)

# Set the minor locator
ax.xaxis.set_minor_locator(AutoMinorLocator())

# Set the tick parameters
ax.tick_params(which='both', width=2)
ax.tick_params(which='major', length=7)
ax.tick_params(which='minor', length=4, color='r')

# Display the plot
plt.show()
```

В этом шаге мы создаем новые данные и строим график для них. Затем мы задаем вторичный делитель шкалы для автоматического определения количества вторичных делений. После этого мы задаем параметры делений шкалы, то есть ширину и длину делений и их цвет, как для основных, так и для вторичных делений. Наконец, мы отображаем график.
