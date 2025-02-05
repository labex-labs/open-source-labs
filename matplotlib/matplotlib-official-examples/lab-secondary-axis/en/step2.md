# Plot the data

We will create a simple sine wave to demonstrate the use of a secondary axis. We will plot the sine wave using degrees as the x-axis.

```python
fig, ax = plt.subplots(layout='constrained')
x = np.arange(0, 360, 1)
y = np.sin(2 * x * np.pi / 180)
ax.plot(x, y)
ax.set_xlabel('angle [degrees]')
ax.set_ylabel('signal')
ax.set_title('Sine wave')
```
