# Definir funciones de preprocesamiento

Un token puede ser una palabra, una parte de una palabra o cualquier cosa comprendida entre espacios o símbolos en una cadena. Aquí definimos una función que extrae los tokens utilizando una expresión regular simple (regex) que coincide con los caracteres de palabras Unicode. Esto incluye la mayoría de los caracteres que pueden ser parte de una palabra en cualquier idioma, así como números y el subrayado:

```python
import re

def tokenize(doc):
    """Extraer tokens de doc.

    Esto utiliza una regex simple que coincide con los caracteres de palabras para dividir las cadenas
    en tokens. Para un enfoque más sistemático, consulte CountVectorizer o
    TfidfVectorizer.
    """
    return (tok.lower() for tok in re.findall(r"\w+", doc))
```

Definimos una función adicional que cuenta la (frecuencia de) ocurrencia de cada token en un documento dado. Devuelve un diccionario de frecuencias para ser utilizado por los vectorizadores.

```python
from collections import defaultdict

def token_freqs(doc):
    """Extraer un diccionario que mapea tokens de doc a sus ocurrencias."""

    freq = defaultdict(int)
    for tok in tokenize(doc):
        freq[tok] += 1
    return freq
```
