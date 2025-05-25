# Configuração de `Logging`

O comportamento de `logging` é configurado separadamente.

```python
# main.py

...

if __name__ == '__main__':
    import logging
    logging.basicConfig(
        filename  = 'app.log',      # Log output file
        level     = logging.INFO,   # Output level
    )
```

Tipicamente, esta é uma configuração única na inicialização do programa. A configuração é separada do código que faz as chamadas de `logging`.
