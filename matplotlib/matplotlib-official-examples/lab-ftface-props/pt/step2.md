# Carregar a Fonte

Nesta etapa, carregaremos a fonte com a qual trabalharemos. Usaremos uma fonte fornecida com o Matplotlib.

```python
font = ft.FT2Font(
    os.path.join(matplotlib.get_data_path(),
                 'fonts/ttf/DejaVuSans-Oblique.ttf'))
```
