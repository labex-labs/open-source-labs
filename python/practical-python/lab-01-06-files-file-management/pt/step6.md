# Exercício 1.28: Outros tipos de "arquivos"

E se você quisesse ler um arquivo que não fosse de texto, como um arquivo de dados compactado com gzip? A função embutida `open()` não o ajudará aqui, mas o Python tem um módulo de biblioteca `gzip` que pode ler arquivos compactados com gzip.

Experimente:

```python
>>> import gzip
>>> with gzip.open('portfolio.csv.gz', 'rt') as f:
    for line in f:
        print(line, end='')

... veja a saída ...
>>>
```

Observação: Incluir o modo de arquivo `'rt'` é crucial aqui. Se você esquecer isso, obterá strings de bytes em vez de strings de texto normais.
