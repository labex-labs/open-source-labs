# 内存占用

现在我们将检查压缩图像的内存使用情况。我们预计压缩后的图像占用的内存比原始图像少 8 倍。

```python
print(f"The number of bytes taken in RAM is {compressed_raccoon_kmeans.nbytes}")
print(f"Compression ratio: {compressed_raccoon_kmeans.nbytes / raccoon_face.nbytes}")
```
