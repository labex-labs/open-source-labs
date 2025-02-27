# Затраты памяти

Теперь мы проверим использование памяти сжатых изображений. Мы ожидаем, что сжатое изображение займет в 8 раз меньше памяти, чем исходное.

```python
print(f"The number of bytes taken in RAM is {compressed_raccoon_kmeans.nbytes}")
print(f"Compression ratio: {compressed_raccoon_kmeans.nbytes / raccoon_face.nbytes}")
```
