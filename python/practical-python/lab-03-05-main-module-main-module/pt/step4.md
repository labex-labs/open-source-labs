# Programas Principais vs. Importações de Bibliotecas

Qualquer arquivo Python pode ser executado como principal ou como uma importação de biblioteca:

```bash
$ python3 prog.py # Running as main
```

```python
import prog   # Running as library import
```

Em ambos os casos, `__name__` é o nome do módulo. No entanto, ele só será definido como `__main__` se estiver sendo executado como principal.

Normalmente, você não quer que as instruções que fazem parte do programa principal sejam executadas em uma importação de biblioteca. Portanto, é comum ter uma verificação `if` no código que pode ser usado de qualquer maneira.

```python
if __name__ == '__main__':
    # Does not execute if loaded with import ...
```
