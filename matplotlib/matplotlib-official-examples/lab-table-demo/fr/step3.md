# Création des étiquettes de ligne

Nous allons créer des étiquettes de ligne pour l'ensemble de données pour représenter le nombre d'années pour lesquelles les pertes ont été enregistrées. Nous utiliserons une compréhension de liste pour créer les étiquettes de ligne.

```python
rows = ['%d year' % x for x in (100, 50, 20, 10, 5)]
```
