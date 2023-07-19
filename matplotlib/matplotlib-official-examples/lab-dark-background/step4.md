# Plot the Data

In this step, we will plot the sample data that we generated in the previous step. We will use a `for` loop to plot multiple sine waves with different phases.

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
