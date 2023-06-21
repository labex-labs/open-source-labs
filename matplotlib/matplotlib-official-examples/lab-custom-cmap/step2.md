# Create a Custom Colormap

We can create a custom mapping for a colormap by creating a dictionary that specifies how the RGB channels change from one end of the colormap to the other.

```python
cdict = {
    'red': (
        (0.0, 0.0, 0.0),
        (0.5, 0.0, 0.1),
        (1.0, 1.0, 1.0),
    ),
    'green': (
        (0.0, 0.0, 0.0),
        (1.0, 0.0, 0.0),
    ),
    'blue': (
        (0.0, 0.0, 1.0),
        (0.5, 0.1, 0.0),
        (1.0, 0.0, 0.0),
    )
}

# create the colormap
blue_red = LinearSegmentedColormap('BlueRed', cdict)
```
