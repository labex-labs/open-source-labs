# Memória Usada

Agora verificaremos o uso de memória das imagens comprimidas. Esperamos que a imagem comprimida ocupe 8 vezes menos memória que a imagem original.

```python
print(f"O número de bytes usados na RAM é {compressed_raccoon_kmeans.nbytes}")
print(f"Razão de compressão: {compressed_raccoon_kmeans.nbytes / raccoon_face.nbytes}")
```
