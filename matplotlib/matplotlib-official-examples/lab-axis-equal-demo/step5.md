# Auto-adjust data limits for equal axis aspect ratio

We can also use the `set_aspect('equal', 'box')` function to auto-adjust the data limits for equal axis aspect ratio.

```python
axs[1, 1].plot(3 * np.cos(an), 3 * np.sin(an))
axs[1, 1].set_aspect('equal', 'box')
axs[1, 1].set_title('still a circle, auto-adjusted data limits', fontsize=10)
```

The resulting plot will show a circle that is still proportional and visually appealing.
