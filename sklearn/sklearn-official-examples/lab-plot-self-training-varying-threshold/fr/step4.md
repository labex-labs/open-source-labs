# Définition des valeurs de seuil

```python
x_values = np.arange(0.4, 1.05, 0.05)
x_values = np.append(x_values, 0.99999)
```

Nous définissons un tableau d valeurs de seuil allant de 0,4 à 1, avec des pas de 0,05. Nous ajoutons ensuite une valeur de seuil très élevée de 0,99999 pour nous assurer d inclure une valeur de seuil qui ne résultera en aucun échantillon auto-étiqueté.
