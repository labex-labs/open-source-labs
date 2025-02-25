# Ajouter des jours à une date

## Problème

Écrivez une fonction `add_days(n, d)` qui prend deux arguments :

- `n` : un entier représentant le nombre de jours à ajouter (si positif) ou soustraire (si négatif) à partir de la date donnée.
- `d` : un argument optionnel représentant la date à laquelle les jours doivent être ajoutés ou soustraits. Si non fourni, la date actuelle devrait être utilisée.

La fonction devrait renvoyer un objet `datetime` représentant la nouvelle date après avoir ajouté ou soustrait le nombre spécifié de jours.

## Exemple

```python
from datetime import date

add_days(5, date(2020, 10, 25)) # renvoie datetime.date(2020, 10, 30)
add_days(-5, date(2020, 10, 25)) # renvoie datetime.date(2020, 10, 20)
```
