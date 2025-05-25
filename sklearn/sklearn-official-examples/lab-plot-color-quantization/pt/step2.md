# Converter a Imagem para Floats e Reformate

Vamos converter a imagem para floats e reformá-la num array numpy 2D para que possa ser processada pelo algoritmo K-Means.

```python
# Converter para floats em vez da codificação inteira de 8 bits padrão.
china = np.array(china, dtype=np.float64) / 255

# Obter as dimensões da imagem
w, h, d = original_shape = tuple(china.shape)
assert d == 3

# Reformate a imagem num array numpy 2D
image_array = np.reshape(china, (w * h, d))
```
