# Carregar a Imagem

Usaremos o método `get_sample_data` da biblioteca `cbook` para carregar uma imagem de exemplo. Este método retorna um objeto semelhante a um arquivo, que podemos passar para `imshow` para exibir a imagem.

```python
with cbook.get_sample_data('grace_hopper.jpg') as image_file:
    image = plt.imread(image_file)
```
