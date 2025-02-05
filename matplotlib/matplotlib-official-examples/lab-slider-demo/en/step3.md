# Create the Initial Graph

Now, we will create the initial graph of the sine wave. We will define the initial parameters for the amplitude and frequency and plot the sine wave using those parameters.

```python
t = np.linspace(0, 1, 1000)
init_amplitude = 5
init_frequency = 3

fig, ax = plt.subplots()
line, = ax.plot(t, f(t, init_amplitude, init_frequency), lw=2)
ax.set_xlabel('Time [s]')
```
