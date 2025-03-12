# Implémentation de la journalisation (logging)

Dans cette étape, nous allons améliorer votre code. Au lieu d'utiliser de simples messages d'impression (`print`), nous allons utiliser le module `logging` de Python pour une journalisation appropriée. La journalisation est un excellent moyen de suivre ce que fait votre programme, notamment lorsqu'il s'agit de gérer les erreurs et de comprendre le flux de votre code.

## Comprendre le module de journalisation

Le module `logging` de Python nous offre un moyen flexible d'envoyer des messages de journalisation depuis nos applications. Il est beaucoup plus puissant que l'utilisation simple d'instructions `print`. Voici ce qu'il peut faire :

1. Différents niveaux de journalisation (DEBUG, INFO, WARNING, ERROR, CRITICAL) : Ces niveaux nous aident à catégoriser l'importance des messages. Par exemple, DEBUG est pour des informations détaillées utiles pendant le développement, tandis que CRITICAL est pour des erreurs graves qui pourraient arrêter le programme.
2. Format de sortie configurable : Nous pouvons décider à quoi ressembleront les messages de journalisation, comme ajouter des horodatages ou d'autres informations utiles.
3. Les messages peuvent être dirigés vers différentes sorties (console, fichiers, etc.) : Nous pouvons choisir d'afficher les messages de journalisation sur la console, de les enregistrer dans un fichier ou même de les envoyer à un serveur distant.
4. Filtrage des journaux en fonction de la gravité : Nous pouvons contrôler quels messages nous voyons en fonction de leur niveau de journalisation.

## Ajout de la journalisation au fichier reader.py

Maintenant, modifions votre code pour utiliser le module de journalisation. Ouvrez le fichier `reader.py`.

Tout d'abord, nous devons importer le module `logging` et configurer un enregistreur (logger) pour ce module. Ajoutez le code suivant en haut du fichier :

```python
import logging

# Set up a logger for this module
logger = logging.getLogger(__name__)
```

L'instruction `import logging` importe le module `logging` afin que nous puissions utiliser ses fonctions. `logging.getLogger(__name__)` crée un enregistreur pour ce module spécifique. L'utilisation de `__name__` garantit que l'enregistreur a un nom unique lié au module.

Ensuite, nous allons modifier la fonction `convert_csv()` pour utiliser la journalisation au lieu d'instructions `print`. Voici le code mis à jour :

```python
def convert_csv(rows, converter, header=True):
    """
    Convert a sequence of rows to an output sequence according to a conversion function.
    """
    if header:
        headers = next(rows)
    else:
        headers = []

    result = []
    for row_idx, row in enumerate(rows, start=1):
        try:
            # Try to convert the row
            result.append(converter(headers, row))
        except Exception as e:
            # Log a warning message for bad rows
            logger.warning(f"Row {row_idx}: Bad row: {row}")
            # Log the reason at debug level
            logger.debug(f"Row {row_idx}: Reason: {str(e)}")
            continue

    return result
```

Les principales modifications sont les suivantes :

- Nous avons remplacé `print()` par `logger.warning()` pour le message d'erreur. De cette façon, le message est enregistré avec le niveau d'avertissement approprié, et nous pouvons contrôler sa visibilité plus tard.
- Nous avons ajouté un nouveau message `logger.debug()` avec des détails sur l'exception. Cela nous donne plus d'informations sur ce qui a mal tourné, mais il n'est affiché que si le niveau de journalisation est défini sur DEBUG ou inférieur.
- `str(e)` convertit l'exception en chaîne de caractères, afin que nous puissions afficher la raison de l'erreur dans le message de journalisation.

Après avoir apporté ces modifications, enregistrez le fichier.

## Test de la journalisation

Testons votre code avec la journalisation activée. Ouvrez l'interpréteur Python en exécutant la commande suivante dans votre terminal :

```bash
python3
```

Une fois que vous êtes dans l'interpréteur Python, exécutez le code suivant :

```python
import logging
import reader

# Configure logging level to see all messages
logging.basicConfig(level=logging.DEBUG)

port = reader.read_csv_as_dicts('missing.csv', types=[str, int, float])
print(f"Number of valid rows processed: {len(port)}")
```

Ici, nous importons d'abord le module `logging` et notre module `reader`. Ensuite, nous définissons le niveau de journalisation sur DEBUG en utilisant `logging.basicConfig(level=logging.DEBUG)`. Cela signifie que nous verrons tous les messages de journalisation, y compris DEBUG, INFO, WARNING, ERROR et CRITICAL. Nous appelons ensuite la fonction `read_csv_as_dicts` du module `reader` et affichons le nombre de lignes valides traitées.

Vous devriez voir une sortie comme celle-ci :

```
WARNING:reader:Row 4: Bad row: ['C', '', '53.08']
DEBUG:reader:Row 4: Reason: invalid literal for int() with base 10: ''
WARNING:reader:Row 7: Bad row: ['DIS', '50', 'N/A']
DEBUG:reader:Row 7: Reason: could not convert string to float: 'N/A'
...
Number of valid rows processed: 20
```

Notez que le module de journalisation ajoute un préfixe à chaque message, indiquant le niveau de journalisation (WARNING/DEBUG) et le nom du module.

Maintenant, voyons ce qui se passe si nous changeons le niveau de journalisation pour n'afficher que les avertissements. Exécutez le code suivant dans l'interpréteur Python :

```python
# Reset the logging configuration
import logging
logging.basicConfig(level=logging.WARNING)

port = reader.read_csv_as_dicts('missing.csv', types=[str, int, float])
```

Cette fois, nous définissons le niveau de journalisation sur WARNING en utilisant `logging.basicConfig(level=logging.WARNING)`. Maintenant, vous ne verrez que les messages WARNING, et les messages DEBUG seront masqués :

```
WARNING:reader:Row 4: Bad row: ['C', '', '53.08']
WARNING:reader:Row 7: Bad row: ['DIS', '50', 'N/A']
...
```

Cela montre l'avantage d'utiliser différents niveaux de journalisation. Nous pouvons contrôler le niveau de détail affiché dans les journaux sans modifier notre code.

Pour quitter l'interpréteur Python, exécutez la commande suivante :

```python
exit()
```

Félicitations ! Vous avez maintenant implémenté une gestion d'exceptions et une journalisation appropriées dans votre programme Python. Cela rend votre code plus fiable et vous fournit de meilleures informations en cas d'erreur.
