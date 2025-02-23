# Créer une fonction d'animation

Nous devons créer une fonction `animate` qui génère de nouvelles données aléatoires et met à jour les hauteurs des rectangles.

```python
def animate(frame_number):
    # simulate new data coming in
    data = np.random.randn(1000)
    n, _ = np.histogram(data, HIST_BINS)
    for count, rect in zip(n, bar_container.patches):
        rect.set_height(count)
    return bar_container.patches
```
