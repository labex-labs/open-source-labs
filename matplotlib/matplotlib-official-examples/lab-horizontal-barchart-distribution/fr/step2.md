# Préparer les données

Nous devons définir les catégories et les résultats du sondage. Dans cet exemple, nous avons un sondage où les gens ont évalué leur accord sur des questions selon une échelle à cinq éléments. Nous définirons les catégories comme `category_names` et les résultats du sondage comme `results`.

```python
category_names = ['Fortement en désaccord', 'Désaccord',
                  'Ni d\'accord ni de désaccord', 'Accord', 'Fortement d\'accord']
results = {
    'Question 1': [10, 15, 17, 32, 26],
    'Question 2': [26, 22, 29, 10, 13],
    'Question 3': [35, 37, 7, 2, 19],
    'Question 4': [32, 11, 9, 15, 33],
    'Question 5': [21, 29, 5, 5, 40],
    'Question 6': [8, 19, 5, 30, 38]
}
```
