# Mise en œuvre de l'enregistrement des sous-classes

En programmation, les importations circulaires peuvent être un problème délicat. Au lieu d'importer directement les classes de formatage, nous pouvons utiliser un modèle d'enregistrement. Dans ce modèle, les sous-classes s'enregistrent auprès de leur classe mère. C'est une méthode courante et efficace pour éviter les importations circulaires.

Tout d'abord, comprenons comment nous pouvons trouver le nom du module d'une classe. Le nom du module est important car nous l'utiliserons dans notre modèle d'enregistrement. Pour ce faire, nous allons exécuter une commande Python dans le terminal.

```bash
cd ~/project/structly
python3 -c "from structly.tableformat.formats.text import TextTableFormatter; print(TextTableFormatter.__module__); print(TextTableFormatter.__module__.split('.')[-1])"
```

Lorsque vous exécutez cette commande, vous verrez une sortie comme celle-ci :

```
structly.tableformat.formats.text
text
```

Cette sortie montre que nous pouvons extraire le nom du module à partir de la classe elle-même. Nous utiliserons ce nom de module plus tard pour enregistrer les sous-classes.

Maintenant, modifions la classe `TableFormatter` dans le fichier `tableformat/formatter.py` pour ajouter un mécanisme d'enregistrement. Ouvrez ce fichier dans l'IDE Web. Nous allons ajouter du code à la classe `TableFormatter`. Ce code nous aidera à enregistrer automatiquement les sous-classes.

```python
class TableFormatter(ABC):
    _formats = { }  # Dictionnaire pour stocker les formatteurs enregistrés

    @classmethod
    def __init_subclass__(cls):
        name = cls.__module__.split('.')[-1]
        TableFormatter._formats[name] = cls

    @abstractmethod
    def headings(self, headers):
        pass

    @abstractmethod
    def row(self, rowdata):
        pass
```

La méthode `__init_subclass__` est une méthode spéciale en Python. Elle est appelée chaque fois qu'une sous-classe de `TableFormatter` est créée. Dans cette méthode, nous extrayons le nom du module de la sous-classe et l'utilisons comme clé pour enregistrer la sous-classe dans le dictionnaire `_formats`.

Ensuite, nous devons modifier la fonction `create_formatter` pour utiliser le dictionnaire d'enregistrement. Cette fonction est chargée de créer le formatteur approprié en fonction du nom donné.

```python
def create_formatter(name, column_formats=None, upper_headers=False):
    formatter_cls = TableFormatter._formats.get(name)
    if not formatter_cls:
        raise RuntimeError('Unknown format %s' % name)

    if column_formats:
        class formatter_cls(ColumnFormatMixin, formatter_cls):
              formats = column_formats

    if upper_headers:
        class formatter_cls(UpperHeadersMixin, formatter_cls):
            pass

    return formatter_cls()
```

Après avoir apporté ces modifications, enregistrez le fichier. Ensuite, testons si le programme fonctionne toujours. Nous allons exécuter le script `stock.py`.

```bash
python3 stock.py
```

Si le programme s'exécute correctement, cela signifie que nos modifications n'ont rien cassé. Maintenant, regardons le contenu du dictionnaire `_formats` pour voir comment l'enregistrement fonctionne.

```bash
python3 -c "from structly.tableformat.formatter import TableFormatter; print(TableFormatter._formats)"
```

Vous devriez voir une sortie comme celle-ci :

```
{'text': <class 'structly.tableformat.formats.text.TextTableFormatter'>, 'csv': <class 'structly.tableformat.formats.csv.CSVTableFormatter'>, 'html': <class 'structly.tableformat.formats.html.HTMLTableFormatter'>}
```

Cette sortie confirme que nos sous-classes sont correctement enregistrées dans le dictionnaire `_formats`. Cependant, nous avons toujours des importations au milieu du fichier. Dans l'étape suivante, nous résoudrons ce problème en utilisant des importations dynamiques.
