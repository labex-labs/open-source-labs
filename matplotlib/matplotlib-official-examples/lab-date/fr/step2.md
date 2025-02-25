# Charger les données

Ensuite, nous allons charger les données que nous souhaitons tracer. Nous utiliserons un tableau enregistré numpy issu des données csv de Yahoo avec les champs date, ouverture, haut, bas, fermeture, volume, fermeture ajustée du répertoire mpl-data/sample_data. Le tableau enregistré stocke la date sous forme d'un np.datetime64 avec une unité de jour ('D') dans la colonne date.

```python
data = cbook.get_sample_data('goog.npz')['price_data']
```
