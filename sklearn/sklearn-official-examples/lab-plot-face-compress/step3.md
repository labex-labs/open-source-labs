# Memory Footprint

We will now check the memory usage of the compressed images. We expect the compressed image to take 8 times less memory than the original image.

```python
print(f"The number of bytes taken in RAM is {compressed_raccoon_kmeans.nbytes}")
print(f"Compression ratio: {compressed_raccoon_kmeans.nbytes / raccoon_face.nbytes}")
```


