# Customize the histogram

In this step, we will customize the histogram by adding labels, title, and adjusting the layout.

```python
ax.set_xlabel('Smarts')
ax.set_ylabel('Probability density')
ax.set_title(r'Histogram of IQ: $\mu=100$, $\sigma=15$')
fig.tight_layout()
plt.show()
```
