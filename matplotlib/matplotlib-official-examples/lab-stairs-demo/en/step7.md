# Create a hatched histogram

```python
plt.stairs(np.arange(1, 6, 1)*0.3, np.arange(2, 8, 1),
              orientation='horizontal', hatch='//',
              label='Hatched histogram\nw/ horizontal orientation')
plt.legend()
plt.show()
```
