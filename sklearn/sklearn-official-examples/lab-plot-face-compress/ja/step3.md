# メモリ使用量

ここでは、圧縮された画像のメモリ使用量を確認します。圧縮された画像は、元の画像よりも8分の1のメモリを使用することが期待されます。

```python
print(f"The number of bytes taken in RAM is {compressed_raccoon_kmeans.nbytes}")
print(f"Compression ratio: {compressed_raccoon_kmeans.nbytes / raccoon_face.nbytes}")
```
