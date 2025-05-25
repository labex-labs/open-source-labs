# Definir funções de pré-processamento

Um token pode ser uma palavra, parte de uma palavra ou qualquer coisa compreendida entre espaços ou símbolos numa string. Aqui, definimos uma função que extrai os tokens usando uma expressão regular (regex) simples que corresponde a caracteres de palavra Unicode. Isto inclui a maioria dos caracteres que podem fazer parte de uma palavra em qualquer língua, bem como números e o sublinhado:

```python
import re

def tokenize(doc):
    """Extrair tokens de doc.

    Isto utiliza uma regex simples que corresponde a caracteres de palavra para dividir as strings em tokens. Para uma abordagem mais fundamentada, consulte CountVectorizer ou TfidfVectorizer.
    """
    return (tok.lower() for tok in re.findall(r"\w+", doc))
```

Definimos uma função adicional que conta a frequência de ocorrência de cada token num documento dado. Retorna um dicionário de frequências a ser usado pelos vectorizadores.

```python
from collections import defaultdict

def token_freqs(doc):
    """Extrair um dicionário que mapeia tokens de doc às suas ocorrências."""

    freq = defaultdict(int)
    for tok in tokenize(doc):
        freq[tok] += 1
    return freq
```
