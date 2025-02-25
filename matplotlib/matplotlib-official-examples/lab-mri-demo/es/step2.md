# Cargar los datos de la imagen de resonancia magnética (MRI)

Utilizaremos la función `get_sample_data` de `matplotlib` para cargar la imagen de muestra de resonancia magnética. La imagen está en formato de enteros de 16 bits de 256x256.

```python
with cbook.get_sample_data('s1045.ima.gz') as dfile:
    im = np.frombuffer(dfile.read(), np.uint16).reshape((256, 256))
```
