# Générer de nouveaux échantillons

Nous utilisons le meilleur estimateur pour échantillonner 44 nouveaux points à partir des données. Nous transformons ensuite les nouvelles données en retournant à sa dimension d'origine de 64 en utilisant l'inverse de la PCA.

```python
# échantillonner 44 nouveaux points à partir des données
new_data = kde.sample(44, random_state=0)
new_data = pca.inverse_transform(new_data)
```
