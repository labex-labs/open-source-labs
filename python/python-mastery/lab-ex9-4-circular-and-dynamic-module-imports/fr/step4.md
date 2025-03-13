# Utilisation des importations dynamiques

En programmation, les importations servent à inclure le code d'autres modules afin que nous puissions utiliser leur fonctionnalité. Cependant, parfois, avoir des importations au milieu d'un fichier peut rendre le code un peu désordonné et difficile à comprendre. Dans cette partie, nous allons apprendre à utiliser les importations dynamiques pour résoudre ce problème. Les importations dynamiques sont une fonctionnalité puissante qui nous permet de charger des modules à l'exécution, ce qui signifie que nous chargeons un module seulement lorsque nous en avons réellement besoin.

Tout d'abord, nous devons supprimer les instructions d'importation actuellement placées après la classe `TableFormatter`. Ces importations sont des importations statiques, qui sont chargées lorsque le programme démarre. Pour ce faire, ouvrez le fichier `tableformat/formatter.py` dans l'IDE Web. Une fois le fichier ouvert, recherchez et supprimez les lignes suivantes :

```python
from .formats.text import TextTableFormatter
from .formats.csv import CSVTableFormatter
from .formats.html import HTMLTableFormatter
```

Si vous essayez d'exécuter le programme maintenant en exécutant la commande suivante dans le terminal :

```bash
python3 stock.py
```

Le programme échouera. La raison en est que les formatteurs ne seront pas enregistrés dans le dictionnaire `_formats`. Vous verrez un message d'erreur concernant un format inconnu. C'est parce que le programme ne peut pas trouver les classes de formatteurs dont il a besoin pour fonctionner correctement.

Pour résoudre ce problème, nous allons modifier la fonction `create_formatter`. L'objectif est d'importer dynamiquement le module requis lorsqu'il est nécessaire. Mettez à jour la fonction comme indiqué ci-dessous :

```python
def create_formatter(name, column_formats=None, upper_headers=False):
    if name not in TableFormatter._formats:
        __import__(f'{__package__}.formats.{name}')

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

La ligne la plus importante de cette fonction est :

```python
__import__(f'{__package__}.formats.{name}')
```

Cette ligne importe dynamiquement le module en fonction du nom du format. Lorsque le module est importé, sa sous-classe de `TableFormatter` s'enregistre automatiquement. Cela est dû à la méthode `__init_subclass__` que nous avons ajoutée précédemment. Cette méthode est une méthode spéciale de Python qui est appelée lorsqu'une sous-classe est créée, et dans notre cas, elle est utilisée pour enregistrer la classe de formatteur.

Après avoir apporté ces modifications, enregistrez le fichier. Ensuite, exécutez le programme à nouveau en utilisant la commande suivante :

```bash
python3 stock.py
```

Le programme devrait maintenant fonctionner correctement, même si nous avons supprimé les importations statiques. Pour vérifier que l'importation dynamique fonctionne comme prévu, nous allons vider le dictionnaire `_formats` puis appeler la fonction `create_formatter`. Exécutez la commande suivante dans le terminal :

```bash
python3 -c "from structly.tableformat.formatter import TableFormatter, create_formatter; TableFormatter._formats.clear(); print('Before:', TableFormatter._formats); create_formatter('text'); print('After:', TableFormatter._formats)"
```

Vous devriez voir une sortie similaire à celle-ci :

```
Before: {}
After: {'text': <class 'structly.tableformat.formats.text.TextTableFormatter'>}
```

Cette sortie confirme que l'importation dynamique charge le module et enregistre la classe de formatteur lorsque cela est nécessaire.

En utilisant les importations dynamiques et l'enregistrement des classes, nous avons créé une structure de code plus propre et plus facilement maintenable. Voici les avantages :

1. Toutes les importations sont maintenant en haut du fichier, ce qui suit les conventions de Python. Cela rend le code plus facile à lire et à comprendre.
2. Nous avons éliminé les importations circulaires. Les importations circulaires peuvent causer des problèmes dans un programme, tels que des boucles infinies ou des erreurs difficiles à déboguer.
3. Le code est plus flexible. Maintenant, nous pouvons ajouter de nouveaux formatteurs sans modifier la fonction `create_formatter`. Cela est très utile dans un scénario réel où de nouvelles fonctionnalités pourraient être ajoutées au fil du temps.

Ce modèle d'utilisation des importations dynamiques et de l'enregistrement des classes est couramment utilisé dans les systèmes de plugins et les frameworks. Dans ces systèmes, les composants doivent être chargés dynamiquement en fonction des besoins de l'utilisateur ou des exigences du programme.
