# Création de la fonction de calcul de la différence en mois

Maintenant que nous savons comment travailler avec les objets de date et calculer la différence en jours, créons une fonction pour calculer la différence en mois.

Dans de nombreuses applications, un mois est approximé à 30 jours. Bien que ce ne soit pas toujours précis (les mois peuvent avoir de 28 à 31 jours), c'est une simplification courante qui fonctionne bien pour de nombreux calculs commerciaux.

Ouvrez votre fichier `month_difference.py` et ajoutez cette fonction sous votre code existant :

```python
def months_diff(start, end):
    """
    Calculate the difference in months between two dates.

    Args:
        start (date): The start date
        end (date): The end date

    Returns:
        int: The number of months between the dates (rounded up)
    """
    # Calculate the difference in days
    days_difference = (end - start).days

    # Convert days to months (assuming 30 days per month) and round up
    months = ceil(days_difference / 30)

    return months
```

Comprenons ce que fait cette fonction :

1. Elle prend deux paramètres : `start` et `end`, qui sont des objets de date
2. Elle calcule la différence en jours entre ces dates
3. Elle divise par 30 pour convertir les jours en mois
4. Elle utilise `ceil()` pour arrondir au nombre entier supérieur
5. Elle retourne le résultat sous forme d'entier

La fonction `ceil()` est utilisée car dans de nombreux scénarios commerciaux, même un mois partiel est compté comme un mois entier pour les facturations.

Pour tester notre fonction, ajoutez le code suivant à la fin de votre fichier :

```python
# Test the months_diff function with our example dates
print(f"Months between {date1} and {date2}: {months_diff(date1, date2)}")

# Test with some other date pairs
print(f"Months between 2020-10-28 and 2020-11-25: {months_diff(date(2020, 10, 28), date(2020, 11, 25))}")
print(f"Months between 2020-12-15 and 2021-01-10: {months_diff(date(2020, 12, 15), date(2021, 01, 10))}")
```

Enregistrez votre fichier et exécutez-le à nouveau :

```bash
python3 ~/project/month_difference.py
```

Vous devriez voir une sortie comme celle-ci :

```
Date 1: 2023-01-15
Date 2: 2023-03-20
Difference in days: 64
Months between 2023-01-15 and 2023-03-20: 3
Months between 2020-10-28 and 2020-11-25: 1
Months between 2020-12-15 and 2021-01-10: 1
```

Remarquez que :

- Les 64 jours entre le 15 janvier 2023 et le 20 mars 2023 sont calculés comme 3 mois (64/30 = 2,13, arrondi à 3)
- La différence entre le 28 octobre et le 25 novembre est calculée comme 1 mois
- La différence entre le 15 décembre et le 10 janvier (au-delà d'une limite d'année) est également calculée comme 1 mois
