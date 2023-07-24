# Plot Data

Now we can plot our data using the `plot` function. We will create two lines using the data we created in step 3.

```python
ax.plot(theta, r, color="tab:orange", lw=3, label="a line")
ax.plot(0.5 * theta, r, color="tab:blue", ls="--", lw=3, label="another line")
```
