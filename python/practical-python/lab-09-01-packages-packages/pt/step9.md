# Outra solução para scripts

Como observado, agora você precisa usar `-m package.module` para executar scripts dentro do seu pacote.

```bash
$ python3 -m porty.pcost portfolio.csv
```

Há outra alternativa: Escrever um novo script de nível superior (top-level).

```python
#!/usr/bin/env python3
# pcost.py
import porty.pcost
import sys
porty.pcost.main(sys.argv)
```

Este script reside _fora_ do pacote. Por exemplo, observando a estrutura de diretórios:

    pcost.py       # script de nível superior (top-level-script)
    porty/         # diretório do pacote
        __init__.py
        pcost.py
        ...
