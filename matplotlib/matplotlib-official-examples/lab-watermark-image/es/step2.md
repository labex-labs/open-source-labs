# Cargar la imagen

A continuación, necesitamos cargar la imagen que queremos superponer en el gráfico. Podemos utilizar el método `get_sample_data` del módulo `matplotlib.cbook` para cargar una imagen de muestra. En este ejemplo, utilizaremos la imagen `logo2.png`.

```python
with cbook.get_sample_data('logo2.png') as file:
    im = image.imread(file)
```
