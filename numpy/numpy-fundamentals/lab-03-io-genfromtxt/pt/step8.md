# Usando Funções de Atalho

O módulo `numpy.lib.npyio` fornece funções de atalho derivadas de `numpy.genfromtxt`. Essas funções têm valores padrão diferentes e retornam um array NumPy padrão ou um array mascarado.

```python
from numpy.lib.npyio import recfromtxt

recfromtxt(StringIO(data), delimiter=",")
```
