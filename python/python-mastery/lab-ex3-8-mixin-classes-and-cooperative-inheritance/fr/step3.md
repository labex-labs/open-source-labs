# Création d'une API conviviale pour les Mixins

Les mixins sont puissants, mais l'utilisation directe de l'héritage multiple peut sembler complexe. Dans cette étape, nous allons améliorer la fonction `create_formatter()` pour masquer cette complexité, en fournissant une API plus facile à utiliser pour les utilisateurs.

Tout d'abord, assurez-vous que `tableformat.py` est ouvert dans votre éditeur :

```bash
cd ~/project
touch tableformat.py
```

Trouvez la fonction `create_formatter()` existante :

```python
# Existing function in tableformat.py
def create_formatter(name):
    """
    Create an appropriate formatter based on the name.
    """
    if name == 'text':
        return TextTableFormatter()
    elif name == 'csv':
        return CSVTableFormatter()
    elif name == 'html':
        return HTMLTableFormatter()
    else:
        raise RuntimeError(f'Unknown format {name}')
```

Remplacez _l'ensemble de la définition de fonction_ `create_formatter()` existante par la version améliorée ci-dessous. Cette nouvelle version accepte des arguments optionnels pour les formats de colonne et la mise en majuscules des en-têtes.

```python
# Replace the old create_formatter with this in tableformat.py

def create_formatter(name, column_formats=None, upper_headers=False):
    """
    Create a formatter with optional enhancements.

    Parameters:
    name : str
        Name of the formatter ('text', 'csv', 'html')
    column_formats : list, optional
        List of format strings for column formatting.
        Note: Relies on ColumnFormatMixin existing above this function.
    upper_headers : bool, optional
        Whether to convert headers to uppercase.
        Note: Relies on UpperHeadersMixin existing above this function.
    """
    if name == 'text':
        formatter_cls = TextTableFormatter
    elif name == 'csv':
        formatter_cls = CSVTableFormatter
    elif name == 'html':
        formatter_cls = HTMLTableFormatter
    else:
        raise RuntimeError(f'Unknown format {name}')

    # Build the inheritance list dynamically
    bases = []
    if column_formats:
        bases.append(ColumnFormatMixin)
    if upper_headers:
        bases.append(UpperHeadersMixin)
    bases.append(formatter_cls) # Base formatter class comes last

    # Create the custom class dynamically
    # Need to ensure ColumnFormatMixin and UpperHeadersMixin are defined before this point
    class CustomFormatter(*bases):
        # Set formats if ColumnFormatMixin is used
        if column_formats:
            formats = column_formats

    return CustomFormatter() # Return an instance of the dynamically created class
```

_Auto-correction : Créez dynamiquement le tuple de classes pour l'héritage au lieu de plusieurs branches if/elif._

Cette fonction améliorée détermine d'abord la classe de formateur de base (`TextTableFormatter`, `CSVTableFormatter`, etc.). Ensuite, en fonction des arguments optionnels `column_formats` et `upper_headers`, elle construit dynamiquement une nouvelle classe (`CustomFormatter`) qui hérite des mixins nécessaires et de la classe de formateur de base. Enfin, elle renvoie une instance de ce formateur personnalisé.

**N'oubliez pas d'enregistrer les modifications apportées à `tableformat.py`.**

Maintenant, testons notre fonction améliorée. **Assurez-vous d'avoir enregistré la fonction `create_formatter` mise à jour dans `tableformat.py`.**

Tout d'abord, testez le formatage des colonnes. Créez `step3_test1.py` :

```python
# step3_test1.py
from tableformat import create_formatter, portfolio, print_table

# Using the same formats as before, subject to type issues.
# Use formats compatible with strings if '%d', '%.2f' cause errors.
formatter = create_formatter('text', column_formats=['%10s', '%10s', '%10.2f'])

print("--- Running Step 3 Test 1 (create_formatter with column_formats) ---")
print_table(portfolio, ['name', 'shares', 'price'], formatter)
print("--------------------------------------------------------------------")
```

Exécutez le script :

```bash
python3 step3_test1.py
```

Vous devriez voir le tableau avec les colonnes formatées (encore une fois, sous réserve de la gestion des types du format de prix) :

```
--- Running Step 3 Test 1 (create_formatter with column_formats) ---
      name     shares      price
---------- ---------- ----------
        AA        100      32.20
       IBM         50      91.10
       CAT        150      83.44
      MSFT        200      51.23
        GE         95      40.37
      MSFT         50      65.10
       IBM        100      70.44
--------------------------------------------------------------------
```

Ensuite, testez les en-têtes en majuscules. Créez `step3_test2.py` :

```python
# step3_test2.py
from tableformat import create_formatter, portfolio, print_table

formatter = create_formatter('text', upper_headers=True)

print("--- Running Step 3 Test 2 (create_formatter with upper_headers) ---")
print_table(portfolio, ['name', 'shares', 'price'], formatter)
print("-------------------------------------------------------------------")
```

Exécutez le script :

```bash
python3 step3_test2.py
```

Vous devriez voir le tableau avec les en-têtes en majuscules :

```
--- Running Step 3 Test 2 (create_formatter with upper_headers) ---
      NAME     SHARES      PRICE
---------- ---------- ----------
        AA        100       32.2
       IBM         50       91.1
       CAT        150      83.44
      MSFT        200      51.23
        GE         95      40.37
      MSFT         50       65.1
       IBM        100      70.44
-------------------------------------------------------------------
```

Enfin, combinez les deux options. Créez `step3_test3.py` :

```python
# step3_test3.py
from tableformat import create_formatter, portfolio, print_table

# Using the same formats as before
formatter = create_formatter('text', column_formats=['%10s', '%10s', '%10.2f'], upper_headers=True)

print("--- Running Step 3 Test 3 (create_formatter with both options) ---")
print_table(portfolio, ['name', 'shares', 'price'], formatter)
print("------------------------------------------------------------------")
```

Cela devrait afficher un tableau avec à la fois des colonnes formatées et des en-têtes en majuscules :

```
--- Running Step 3 Test 3 (create_formatter with both options) ---
      NAME     SHARES      PRICE
---------- ---------- ----------
        AA        100      32.20
       IBM         50      91.10
       CAT        150      83.44
      MSFT        200      51.23
        GE         95      40.37
      MSFT         50      65.10
       IBM        100      70.44
------------------------------------------------------------------
```

La fonction améliorée fonctionne également avec d'autres types de formateurs. Par exemple, essayez-la avec le formateur CSV. Créez `step3_test4.py` :

```python
# step3_test4.py
from tableformat import create_formatter, portfolio, print_table

# For CSV, ensure formats produce valid CSV fields.
# Adding quotes around the string name field.
formatter = create_formatter('csv', column_formats=['"%s"', '%d', '%.2f'], upper_headers=True)

print("--- Running Step 3 Test 4 (create_formatter with CSV) ---")
print_table(portfolio, ['name', 'shares', 'price'], formatter)
print("---------------------------------------------------------")
```

Exécutez le script :

```bash
python3 step3_test4.py
```

Cela devrait produire des en-têtes en majuscules et des colonnes formatées au format CSV (encore une fois, problème de type potentiel pour le formatage `%d`/`%.2f` sur les chaînes transmises par `print_table`) :

```
--- Running Step 3 Test 4 (create_formatter with CSV) ---
NAME,SHARES,PRICE
"AA",100,32.20
"IBM",50,91.10
"CAT",150,83.44
"MSFT",200,51.23
"GE",95,40.37
"MSFT",50,65.10
"IBM",100,70.44
---------------------------------------------------------
```

En améliorant la fonction `create_formatter()`, nous avons créé une API conviviale. Les utilisateurs peuvent désormais facilement appliquer les fonctionnalités des mixins sans avoir à gérer eux-mêmes la structure d'héritage multiple.
