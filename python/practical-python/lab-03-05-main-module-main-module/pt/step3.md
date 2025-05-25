# Verificação `__main__`

É prática padrão para módulos que são executados como um script principal usar esta convenção:

```python
# prog.py
...
if __name__ == '__main__':
    # Running as the main program ...
    statements
    ...
```

As instruções contidas dentro da declaração `if` se tornam o programa _main_.
