# Charger une police

Dans cette étape, nous allons charger la police avec laquelle nous allons travailler. Nous utiliserons une police livrée avec Matplotlib.

```python
font = ft.FT2Font(
    os.path.join(matplotlib.get_data_path(),
                 'fonts/ttf/DejaVuSans-Oblique.ttf'))
```
