# Variáveis de Ambiente (Environment Variables)

As variáveis de ambiente são definidas no shell.

```bash
$ export NAME dave
$ export RSH ssh
$ python3 prog.py
```

`os.environ` é um dicionário que contém esses valores.

```python
import os

name = os.environ['NAME'] # 'dave'
```

As alterações são refletidas em quaisquer subprocessos posteriormente lançados pelo programa.
