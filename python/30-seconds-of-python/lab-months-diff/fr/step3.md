# Tests avec divers scénarios de dates

Pour mieux comprendre comment notre fonction `months_diff` fonctionne avec différents scénarios de dates, créons un fichier de test séparé. Cette approche est courante dans le développement logiciel pour vérifier que notre code fonctionne comme prévu.

Créez un nouveau fichier appelé `month_diff_test.py` dans le répertoire `/home/labex/project` :

```python
from datetime import date
from month_difference import months_diff

# Test scenario 1: Dates in the same month
date1 = date(2023, 5, 5)
date2 = date(2023, 5, 25)
print(f"Same month: {months_diff(date1, date2)} month(s)")

# Test scenario 2: Consecutive months
date3 = date(2023, 6, 28)
date4 = date(2023, 7, 15)
print(f"Consecutive months: {months_diff(date3, date4)} month(s)")

# Test scenario 3: Dates crossing year boundary
date5 = date(2023, 12, 20)
date6 = date(2024, 1, 10)
print(f"Across years: {months_diff(date5, date6)} month(s)")

# Test scenario 4: Several months apart
date7 = date(2023, 3, 10)
date8 = date(2023, 9, 20)
print(f"Several months: {months_diff(date7, date8)} month(s)")

# Test scenario 5: Dates in reverse order (negative result)
print(f"Reverse order: {months_diff(date8, date7)} month(s)")

# Test scenario 6: Exact multiples of 30 days
date9 = date(2023, 1, 1)
date10 = date(2023, 1, 31)  # 30 days
date11 = date(2023, 3, 2)   # 60 days
print(f"30 days exactly: {months_diff(date9, date10)} month(s)")
print(f"60 days exactly: {months_diff(date9, date11)} month(s)")
```

Enregistrez ce fichier et exécutez-le :

```bash
python3 ~/project/month_diff_test.py
```

Vous devriez voir une sortie similaire à :

```
Same month: 1 month(s)
Consecutive months: 1 month(s)
Across years: 1 month(s)
Several months: 7 month(s)
Reverse order: -7 month(s)
30 days exactly: 1 month(s)
60 days exactly: 2 month(s)
```

Analysons ces résultats :

1. **Même mois** : Même dans le même mois, notre fonction retourne 1 mois. C'est parce que même un mois partiel est compté comme un mois entier.

2. **Mois consécutifs** : Pour des dates dans des mois consécutifs, la fonction retourne 1 mois.

3. **Au-delà des années** : Pour des dates qui traversent la limite d'année, la fonction calcule toujours correctement.

4. **Plusieurs mois** : Pour des dates séparées de plusieurs mois, la fonction calcule le nombre approprié de mois.

5. **Ordre inverse** : Lorsque la date de fin est antérieure à la date de début, nous obtenons un résultat négatif, ce qui est logique pour des scénarios tels que le calcul du temps restant.

6. **Multiples exacts** : Pour exactement 30 jours, nous obtenons 1 mois. Pour 60 jours, nous obtenons 2 mois. Cela confirme que notre fonction fonctionne comme prévu avec des multiples exacts de notre définition de mois.

Notre fonction `months_diff` gère correctement tous ces cas de test selon notre définition d'un mois comme étant de 30 jours.
