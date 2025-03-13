# Explorer les importations circulaires

Une importation circulaire est une situation où deux modules ou plus dépendent les uns des autres. Plus précisément, lorsque le module A importe le module B, et que le module B importe également le module A, soit directement, soit indirectement. Cela crée une boucle de dépendance que le système d'importation de Python ne peut pas résoudre correctement. En termes plus simples, Python reste bloqué dans une boucle en essayant de déterminer quel module importer en premier, ce qui peut entraîner des erreurs dans votre programme.

Expérimentons avec notre code pour voir comment les importations circulaires peuvent causer des problèmes.

Tout d'abord, nous allons exécuter le programme de gestion des stocks pour vérifier s'il fonctionne avec la structure actuelle. Cette étape nous permet d'établir une référence et de voir le programme fonctionner comme prévu avant d'apporter des modifications.

```bash
cd ~/project/structly
python3 stock.py
```

Le programme devrait s'exécuter correctement et afficher les données des stocks dans un tableau formaté. Si c'est le cas, cela signifie que la structure actuelle du code fonctionne bien sans aucun problème d'importation circulaire.

Maintenant, nous allons modifier le fichier `formatter.py`. En général, il est recommandé de déplacer les importations en haut d'un fichier. Cela rend le code plus organisé et plus facile à comprendre d'un coup d'œil.

```bash
cd ~/project/structly
```

Ouvrez `tableformat/formatter.py` dans l'IDE Web. Nous allons déplacer les importations suivantes en haut du fichier, juste après les importations existantes. Ces importations concernent différents formatteurs de tableaux, comme le format texte, CSV et HTML.

```python
from .formats.text import TextTableFormatter
from .formats.csv import CSVTableFormatter
from .formats.html import HTMLTableFormatter
```

Le début du fichier devrait maintenant ressembler à ceci :

```python
# formatter.py
from abc import ABC, abstractmethod
from .mixins import ColumnFormatMixin, UpperHeadersMixin
from .formats.text import TextTableFormatter
from .formats.csv import CSVTableFormatter
from .formats.html import HTMLTableFormatter

class TableFormatter(ABC):
    @abstractmethod
    def headings(self, headers):
        pass

    @abstractmethod
    def row(self, rowdata):
        pass
```

Enregistrez le fichier et essayez d'exécuter à nouveau le programme de gestion des stocks.

```bash
python3 stock.py
```

Vous devriez voir un message d'erreur indiquant que `TableFormatter` n'est pas défini. Ceci est un signe clair d'un problème d'importation circulaire.

Le problème se produit en raison de la chaîne d'événements suivante :

1. `formatter.py` essaie d'importer `TextTableFormatter` depuis `formats/text.py`.
2. `formats/text.py` importe `TableFormatter` depuis `formatter.py`.
3. Lorsque Python essaie de résoudre ces importations, il reste bloqué dans une boucle car il ne peut pas décider quel module importer entièrement en premier.

Revenons en arrière sur nos modifications pour que le programme fonctionne à nouveau. Modifiez `tableformat/formatter.py` et replacez les importations à leur emplacement d'origine (après la définition de la classe `TableFormatter`).

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
```

Exécutez le programme à nouveau pour confirmer qu'il fonctionne.

```bash
python3 stock.py
```

Cela démontre que même si avoir des importations au milieu du fichier n'est pas la meilleure pratique en termes d'organisation du code, cela a été fait pour éviter un problème d'importation circulaire. Dans les étapes suivantes, nous explorerons de meilleures solutions.
