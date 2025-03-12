# Ajout de la fonctionnalité de conversion de lignes

En programmation, il est souvent utile de créer des instances d'une classe à partir de lignes de données, notamment lorsqu'on manipule des données issues de sources telles que des fichiers CSV. Dans cette section, nous allons ajouter la capacité de créer des instances de la classe `Structure` à partir de lignes de données. Nous allons le faire en implémentant une méthode de classe `from_row` dans la classe `Structure`.

1. Tout d'abord, vous devez ouvrir le fichier `structure.py`. C'est là que nous allons apporter des modifications à notre code. Utilisez la commande suivante dans votre terminal :

```bash
code ~/project/structure.py
```

2. Ensuite, nous allons modifier la fonction `validate_attributes`. Cette fonction est un décorateur de classe qui extrait les instances de `Validator` et construit automatiquement les listes `_fields` et `_types`. Nous allons la mettre à jour pour collecter également les informations de type.

```python
def validate_attributes(cls):
    """
    Class decorator that extracts Validator instances
    and builds the _fields and _types lists automatically
    """
    validators = []
    for name, val in vars(cls).items():
        if isinstance(val, Validator):
            validators.append(val)

    # Set _fields based on validator names
    cls._fields = [val.name for val in validators]

    # Set _types based on validator expected_types
    cls._types = [getattr(val, 'expected_type', lambda x: x) for val in validators]

    # Create initialization method
    cls.create_init()

    return cls
```

Dans cette fonction mise à jour, nous collectons l'attribut `expected_type` de chaque validateur et le stockons dans la variable de classe `_types`. Cela sera utile plus tard lorsque nous convertirons les données des lignes en types appropriés.

3. Maintenant, nous allons ajouter la méthode de classe `from_row` à la classe `Structure`. Cette méthode nous permettra de créer une instance de la classe à partir d'une ligne de données, qui peut être une liste ou un tuple.

```python
@classmethod
def from_row(cls, row):
    """
    Create an instance from a data row (list or tuple)
    """
    rowdata = [func(val) for func, val in zip(cls._types, row)]
    return cls(*rowdata)
```

Voici comment cette méthode fonctionne :

- Elle prend une ligne de données, qui peut être sous forme de liste ou de tuple.
- Elle convertit chaque valeur de la ligne en le type attendu en utilisant la fonction correspondante de la liste `_types`.
- Elle crée ensuite et retourne une nouvelle instance de la classe en utilisant les valeurs converties.

4. Après avoir apporté ces modifications, enregistrez le fichier `structure.py`. Cela garantit que vos modifications de code sont conservées.

5. Testons notre méthode `from_row` pour nous assurer qu'elle fonctionne comme prévu. Nous allons créer un test simple en utilisant la classe `Stock`. Exécutez la commande suivante dans votre terminal :

```bash
cd ~/project
python3 -c "from stock import Stock; s = Stock.from_row(['GOOG', '100', '490.1']); print(s); print(f'Cost: {s.cost}')"
```

Vous devriez voir une sortie similaire à celle-ci :

```
Stock('GOOG', 100, 490.1)
Cost: 49010.0
```

Notez que les valeurs sous forme de chaînes de caractères '100' et '490.1' ont été automatiquement converties en types appropriés (entier et flottant). Cela montre que notre méthode `from_row` fonctionne correctement.

6. Enfin, essayons de lire des données à partir d'un fichier CSV en utilisant notre module `reader.py`. Exécutez la commande suivante dans votre terminal :

```bash
cd ~/project
python3 -c "from stock import Stock; import reader; portfolio = reader.read_csv_as_instances('portfolio.csv', Stock); print(portfolio); print(f'Total value: {sum(s.cost for s in portfolio)}')"
```

Vous devriez voir une sortie montrant les actions du fichier CSV :

```
[Stock('GOOG', 100, 490.1), Stock('AAPL', 50, 545.75), Stock('MSFT', 200, 30.47)]
Total value: 73444.0
```

La méthode `from_row` nous permet de convertir facilement les données CSV en instances de la classe `Stock`. Associée à la fonction `read_csv_as_instances`, elle constitue un moyen puissant de charger et de manipuler des données structurées.
