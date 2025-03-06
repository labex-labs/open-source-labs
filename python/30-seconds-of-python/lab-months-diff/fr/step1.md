# Comprendre les objets de date en Python

Avant de calculer la différence en mois entre des dates, nous devons comprendre comment travailler avec les objets de date en Python. Dans cette étape, nous allons apprendre à propos du module `datetime` et créer quelques objets de date.

Tout d'abord, créons un nouveau fichier Python dans le répertoire du projet. Ouvrez le WebIDE et cliquez sur l'icône "Nouveau fichier" dans le panneau d'exploration à gauche. Nommez le fichier `month_difference.py` et enregistrez-le dans le répertoire `/home/labex/project`.

Maintenant, ajoutez le code suivant pour importer les modules nécessaires :

```python
from datetime import date
from math import ceil

# Create example date objects
date1 = date(2023, 1, 15)  # 15 janvier 2023
date2 = date(2023, 3, 20)  # 20 mars 2023

# Print the dates to see their format
print(f"Date 1: {date1}")
print(f"Date 2: {date2}")

# Calculate the difference in days
day_difference = (date2 - date1).days
print(f"Difference in days: {day_difference}")
```

Enregistrez le fichier et exécutez-le en utilisant le terminal :

```bash
python3 ~/project/month_difference.py
```

Vous devriez voir une sortie similaire à ceci :

```
Date 1: 2023-01-15
Date 2: 2023-03-20
Difference in days: 64
```

La classe `date` du module `datetime` nous permet de créer des objets de date en spécifiant l'année, le mois et le jour. Lorsque nous soustrayons une date d'une autre, Python retourne un objet `timedelta`. Nous pouvons accéder au nombre de jours dans cet objet en utilisant l'attribut `.days`.

Dans cet exemple, il y a 64 jours entre le 15 janvier 2023 et le 20 mars 2023.
