# Create Animation Function

We need to create an `animate` function that generates new random data and updates the heights of rectangles.

```python
def animate(frame_number):
    # simulate new data coming in
    data = np.random.randn(1000)
    n, _ = np.histogram(data, HIST_BINS)
    for count, rect in zip(n, bar_container.patches):
        rect.set_height(count)
    return bar_container.patches
```
