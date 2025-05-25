# A linha `#!`

No Unix, a linha `#!` pode iniciar um script como Python. Adicione o seguinte à primeira linha do seu arquivo de script.

```python
#!/usr/bin/env python3
#./prog.py
...
```

Ela requer a permissão de executável.

```bash
$ chmod +x prog.py
# Então você pode executar
$ ./prog.py
... output ...
```

_Nota: O Python Launcher no Windows também procura a linha `#!` para indicar a versão da linguagem._
