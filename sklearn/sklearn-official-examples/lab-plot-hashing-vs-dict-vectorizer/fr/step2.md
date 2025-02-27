# Définir les fonctions de prétraitement

Un jeton peut être un mot, une partie de mot ou tout ce qui se trouve entre espaces ou symboles dans une chaîne. Ici, nous définissons une fonction qui extrait les jetons à l'aide d'une expression régulière simple (regex) qui correspond aux caractères de mot Unicode. Cela inclut la plupart des caractères qui peuvent faire partie d'un mot dans n'importe quelle langue, ainsi que les nombres et le tiret bas :

```python
import re

def tokenize(doc):
    """Extraire les jetons à partir de doc.

    Cela utilise une regex simple qui correspond aux caractères de mot pour diviser les chaînes
    en jetons. Pour une approche plus rigoureuse, voir CountVectorizer ou
    TfidfVectorizer.
    """
    return (tok.lower() for tok in re.findall(r"\w+", doc))
```

Nous définissons une fonction supplémentaire qui compte l'occurrence (fréquence) de chaque jeton dans un document donné. Elle renvoie un dictionnaire de fréquences à utiliser par les vectoriseurs.

```python
from collections import defaultdict

def token_freqs(doc):
    """Extraire un dictionnaire qui associe les jetons de doc à leur nombre d'occurrences."""

    freq = defaultdict(int)
    for tok in tokenize(doc):
        freq[tok] += 1
    return freq
```
