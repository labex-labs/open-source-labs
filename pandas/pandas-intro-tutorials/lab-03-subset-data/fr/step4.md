# Filtrer des lignes spécifiques

Pour sélectionner des lignes en fonction d'une expression conditionnelle, utilisez la condition à l'intérieur des crochets de sélection `[]`.

```python
# Filtre les lignes où 'Age' est supérieur à 35
above_35 = titanic[titanic["Age"] > 35]

# Affiche les 5 premières lignes
above_35.head()
```
