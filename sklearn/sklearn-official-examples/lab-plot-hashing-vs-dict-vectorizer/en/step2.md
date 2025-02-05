# Define preprocessing functions

A token may be a word, part of a word or anything comprised between spaces or symbols in a string. Here we define a function that extracts the tokens using a simple regular expression (regex) that matches Unicode word characters. This includes most characters that can be part of a word in any language, as well as numbers and the underscore:

```python
import re

def tokenize(doc):
    """Extract tokens from doc.

    This uses a simple regex that matches word characters to break strings
    into tokens. For a more principled approach, see CountVectorizer or
    TfidfVectorizer.
    """
    return (tok.lower() for tok in re.findall(r"\w+", doc))
```

We define an additional function that counts the (frequency of) occurrence of each token in a given document. It returns a frequency dictionary to be used by the vectorizers.

```python
from collections import defaultdict

def token_freqs(doc):
    """Extract a dict mapping tokens from doc to their occurrences."""

    freq = defaultdict(int)
    for tok in tokenize(doc):
        freq[tok] += 1
    return freq
```
