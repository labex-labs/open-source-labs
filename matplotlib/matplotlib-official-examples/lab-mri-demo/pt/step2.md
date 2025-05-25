# Carregar os dados da imagem de ressonância magnética (MRI)

Usaremos a função `get_sample_data` do `matplotlib` para carregar a imagem de ressonância magnética de exemplo. A imagem está no formato inteiro de 16 bits de 256x256.

```python
with cbook.get_sample_data('s1045.ima.gz') as dfile:
    im = np.frombuffer(dfile.read(), np.uint16).reshape((256, 256))
```
