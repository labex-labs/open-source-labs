# Convert the image into a graph

We will use `img_to_graph` from `sklearn.feature_extraction.image` to convert the image into a graph. The value of the gradient on the edges will also be computed.

```python
from sklearn.feature_extraction import image

graph = image.img_to_graph(img, mask=mask)
```
