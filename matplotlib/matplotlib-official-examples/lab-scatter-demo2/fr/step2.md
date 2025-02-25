# Charger les données

Nous allons charger un tableau enregistré numpy à partir de données csv Yahoo avec les champs date, ouverture, haut, bas, fermeture, volume, fermeture ajustée à partir du répertoire mpl-data/sample_data. Le tableau enregistré stocke la date sous forme d'un np.datetime64 avec une unité de jour ('D') dans la colonne date.

```python
import matplotlib.cbook as cbook

price_data = cbook.get_sample_data('goog.npz')['price_data'].view(np.recarray)
price_data = price_data[-250:]  # obtenir les 250 derniers jours de négociation
```
