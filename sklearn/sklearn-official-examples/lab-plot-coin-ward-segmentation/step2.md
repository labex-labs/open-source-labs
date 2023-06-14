# Define Structure of the Data

Pixels in an image are connected to their neighbors. In order to perform hierarchical clustering on an image, we need to define the structure of the data. We can use scikit-learn's `grid_to_graph` function to create a connectivity matrix that defines the structure of the data.

```python
from sklearn.feature_extraction.image import grid_to_graph

connectivity = grid_to_graph(*rescaled_coins.shape)
```


