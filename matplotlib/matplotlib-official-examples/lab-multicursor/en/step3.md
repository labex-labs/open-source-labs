# Creating Plots

Now, we will create three subplots using the `plt.subplots` function. Two plots will be created in one figure, while the third plot will be created in a separate figure.

```python
fig, (ax1, ax2) = plt.subplots(2, sharex=True)
ax1.plot(t, s1)
ax2.plot(t, s2)
fig, ax3 = plt.subplots()
ax3.plot(t, s3)
```
