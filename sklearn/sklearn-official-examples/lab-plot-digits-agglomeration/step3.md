# Define Connectivity Matrix

In this step, we will define the connectivity matrix using the `grid_to_graph` function from scikit-learn. This function creates a connectivity graph based on the pixel grid of the images.

```python
connectivity = grid_to_graph(*images[0].shape)
```


