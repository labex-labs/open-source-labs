# Load the MRI image data

We will use the `get_sample_data` function from `matplotlib` to load the sample MRI image. The image is in 256x256 16-bit integer format.

```python
with cbook.get_sample_data('s1045.ima.gz') as dfile:
    im = np.frombuffer(dfile.read(), np.uint16).reshape((256, 256))
```
