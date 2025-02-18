# Charger une image

Ensuite, nous devons charger l'image que nous souhaitons superposer sur le graphique. Nous pouvons utiliser la méthode `get_sample_data` du module `matplotlib.cbook` pour charger une image d'exemple. Dans cet exemple, nous utiliserons l'image `logo2.png`.

```python
with cbook.get_sample_data('logo2.png') as file:
    im = image.imread(file)
```
