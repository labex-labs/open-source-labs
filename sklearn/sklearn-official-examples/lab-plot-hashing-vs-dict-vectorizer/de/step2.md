# Definiere Vorverarbeitungfunktionen

Ein Token kann ein Wort, ein Teil eines Worts oder alles sein, was zwischen Leerzeichen oder Symbolen in einer Zeichenkette enthalten ist. Hier definieren wir eine Funktion, die die Tokens mit Hilfe eines einfachen regulären Ausdrucks (Regex) extrahiert, der Unicode-Wortzeichen übereinstimmt. Dies umfasst die meisten Zeichen, die Teil eines Worts in jeder Sprache sein können, sowie Zahlen und das Unterstrich-Zeichen:

```python
import re

def tokenize(doc):
    """Extrahiert Tokens aus doc.

    Dies verwendet einen einfachen Regex, der Wortzeichen übereinstimmt, um Zeichenketten
    in Tokens aufzuteilen. Für einen prinzipielleren Ansatz siehe CountVectorizer oder
    TfidfVectorizer.
    """
    return (tok.lower() for tok in re.findall(r"\w+", doc))
```

Wir definieren eine zusätzliche Funktion, die die Anzahl der Vorkommen (Häufigkeit) jedes Tokens in einem gegebenen Dokument zählt. Sie gibt ein Häufigkeitswörterbuch zurück, das von den Vektorizern verwendet werden soll.

```python
from collections import defaultdict

def token_freqs(doc):
    """Extrahiert ein Dict, das Tokens aus doc auf ihre Vorkommen abbildet."""

    freq = defaultdict(int)
    for tok in tokenize(doc):
        freq[tok] += 1
    return freq
```
