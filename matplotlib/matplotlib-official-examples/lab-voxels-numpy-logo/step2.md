# Define the explode function

Next, we define a function called `explode` that will be used to upscale the voxel image of the NumPy logo. This function takes in a NumPy array as its input and returns a new NumPy array that is twice the size of the input array.

```python
def explode(data):
    size = np.array(data.shape)*2
    data_e = np.zeros(size - 1, dtype=data.dtype)
    data_e[::2, ::2, ::2] = data
    return data_e
```
