# Plot a circle with unequal axis aspect ratio

We will first plot a circle with unequal axis aspect ratio to demonstrate the importance of setting equal axis aspect ratios.

```python
an = np.linspace(0, 2 * np.pi, 100)
fig, axs = plt.subplots(2, 2)

axs[0, 0].plot(3 * np.cos(an), 3 * np.sin(an))
axs[0, 0].set_title('not equal, looks like ellipse', fontsize=10)
```

The resulting plot will show a circle that appears elongated due to the unequal axis aspect ratio.
