# Преобразование изображения в граф с значением градиента на рёбрах

Мы преобразуем изображение в граф с значением градиента на рёбрах. Чем меньше beta, тем более независимой от исходного изображения будет сегментация. При beta = 1 сегментация будет близка к вороной.

```python
# Convert the image into a graph with the value of the gradient on the
# edges.
graph = image.img_to_graph(rescaled_coins)

# Take a decreasing function of the gradient: an exponential
beta = 10
eps = 1e-6
graph.data = np.exp(-beta * graph.data / graph.data.std()) + eps
```
