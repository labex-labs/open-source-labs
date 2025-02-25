# Trier les lignes d'un tableau

Triez le jeu de données Titanic selon l'âge des passagers, puis par classe de cabine et âge dans l'ordre décroissant.

```python
# Trier par Age
titanic.sort_values(by="Age").head()

# Trier par Pclass et Age dans l'ordre décroissant
titanic.sort_values(by=['Pclass', 'Age'], ascending=False).head()
```
