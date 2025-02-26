# Introduction

Les classes peuvent définir des méthodes spéciales. Ces méthodes ont un sens particulier pour l'interpréteur Python. Elles sont toujours précédées et suivies de `__`. Par exemple `__init__`.

```python
class Stock(object):
    def __init__(self):
     ...
    def __repr__(self):
     ...
```

Il existe des dizaines de méthodes spéciales, mais nous ne considérerons que quelques exemples spécifiques.
