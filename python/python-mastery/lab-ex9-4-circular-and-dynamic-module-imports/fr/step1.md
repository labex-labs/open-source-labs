# Comprendre le problème d'importation

Commençons par comprendre ce que sont les importations de modules. En Python, lorsque vous souhaitez utiliser des fonctions, des classes ou des variables provenant d'un autre fichier (module), vous utilisez l'instruction `import`. Cependant, la manière dont vous structurez vos importations peut entraîner divers problèmes.

Maintenant, nous allons examiner un exemple de structure de module problématique. Le code dans `tableformat/formatter.py` contient des importations réparties dans tout le fichier. Cela peut ne pas sembler être un gros problème au premier abord, mais cela crée des problèmes de maintenance et de dépendance.

Tout d'abord, ouvrez l'explorateur de fichiers de l'IDE Web et accédez au répertoire `structly`. Nous allons exécuter quelques commandes pour comprendre la structure actuelle du projet. La commande `cd` est utilisée pour changer le répertoire de travail actuel, et la commande `ls -la` liste tous les fichiers et répertoires dans le répertoire actuel, y compris les fichiers cachés.

```bash
cd ~/project/structly
ls -la
```

Cela vous montrera les fichiers dans le répertoire du projet. Maintenant, nous allons examiner l'un des fichiers problématiques en utilisant la commande `cat`, qui affiche le contenu d'un fichier.

```bash
cat tableformat/formatter.py
```

Vous devriez voir un code similaire au suivant :

```python
# formatter.py
from abc import ABC, abstractmethod
from .mixins import ColumnFormatMixin, UpperHeadersMixin

class TableFormatter(ABC):
    @abstractmethod
    def headings(self, headers):
        pass

    @abstractmethod
    def row(self, rowdata):
        pass

from .formats.text import TextTableFormatter
from .formats.csv import CSVTableFormatter
from .formats.html import HTMLTableFormatter

def create_formatter(name, column_formats=None, upper_headers=False):
    if name == 'text':
        formatter_cls = TextTableFormatter
    elif name == 'csv':
        formatter_cls = CSVTableFormatter
    elif name == 'html':
        formatter_cls = HTMLTableFormatter
    else:
        raise RuntimeError('Unknown format %s' % name)

    if column_formats:
        class formatter_cls(ColumnFormatMixin, formatter_cls):
              formats = column_formats

    if upper_headers:
        class formatter_cls(UpperHeadersMixin, formatter_cls):
            pass

    return formatter_cls()
```

Remarquez l'emplacement des instructions d'importation au milieu du fichier. Cela pose problème pour plusieurs raisons :

1. Cela rend le code plus difficile à lire et à maintenir. Lorsque vous regardez un fichier, vous vous attendez à voir toutes les importations au début afin de pouvoir rapidement comprendre quels modules externes le fichier dépend.
2. Cela peut entraîner des problèmes d'importation circulaire. Les importations circulaires se produisent lorsque deux modules ou plus dépendent les uns des autres, ce qui peut causer des erreurs et faire que votre code se comporte de manière inattendue.
3. Cela viole la convention Python consistant à placer toutes les importations en haut d'un fichier. Suivre les conventions rend votre code plus lisible et plus facile à comprendre pour les autres développeurs.

Dans les étapes suivantes, nous explorerons ces problèmes plus en détail et apprendrons à les résoudre.
