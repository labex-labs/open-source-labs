# Create the Plot

Now that we have our data, we can create our plot. We will begin by creating an axes object using `matplotlib.pyplot.subplots()`. We will then plot our first set of data on this axes object and set the label color to red.

```python
fig, ax1 = plt.subplots()

color = 'tab:red'
ax1.set_xlabel('time (s)')
ax1.set_ylabel('exp', color=color)
ax1.plot(t, data1, color=color)
ax1.tick_params(axis='y', labelcolor=color)
```

Next, we will instantiate a second axes object that shares the same x-axis as the first axes object using the `ax1.twinx()` method. We will then plot our second set of data on this new axes object and set the label color to blue.

```python
ax2 = ax1.twinx()

color = 'tab:blue'
ax2.set_ylabel('sin', color=color)
ax2.plot(t, data2, color=color)
ax2.tick_params(axis='y', labelcolor=color)
```

Finally, we will adjust the layout of our plot using the `fig.tight_layout()` method and display it using `matplotlib.pyplot.show()`.

```python
fig.tight_layout()
plt.show()
```
