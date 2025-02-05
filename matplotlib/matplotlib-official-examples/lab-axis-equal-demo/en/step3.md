# Plot a circle with equal axis aspect ratio

To set the equal axis aspect ratio, we can use the `axis('equal')` function.

```python
axs[0, 1].plot(3 * np.cos(an), 3 * np.sin(an))
axs[0, 1].axis('equal')
axs[0, 1].set_title('equal, looks like circle', fontsize=10)
```

The resulting plot will show a circle that is proportional and visually appealing.
