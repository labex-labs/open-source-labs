# Adjust plot limits while maintaining equal axis aspect ratio

We can also adjust the plot limits while maintaining the equal axis aspect ratio.

```python
axs[1, 0].plot(3 * np.cos(an), 3 * np.sin(an))
axs[1, 0].axis('equal')
axs[1, 0].set(xlim=(-3, 3), ylim=(-3, 3))
axs[1, 0].set_title('still a circle, even after changing limits', fontsize=10)
```

The resulting plot will show a circle that is still proportional even after we change the limits.
